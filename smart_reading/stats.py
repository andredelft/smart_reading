import nltk
from matplotlib import pyplot as plt
import numpy as np
import networkx as nx
import re

def noun_fdist(book, named_entities = True, exceptions = []):
    # NB: named entity exclusion is based on NLTK's ne_chunk procedure, which
    # does not always work perfectly. See for example smart_reading.book.sample(),
    # which still includes 'Descartes', even when named_entities = False
    nouns = []
    if 'entities' in book.__dict__:
        for child in book.entities:
            if type(child) == nltk.tree.Tree and named_entities:
                nouns.append(' '.join(name.capitalize() for name,tag in child))
            elif type(child) == tuple:
                if 'NN' in child[1]:
                    nouns.append(child[0].capitalize())
    else:
        if not named_entities:
            print('\nWarning: named entity exclusion not supported in current Python version\n'
                  'Will continue with regular procedure instead\n')
        nouns = [word.capitalize() for word,tag in book._tags if 'NN' in tag]
        
    nouns = [word for word in nouns if re.search('[a-zA-Z]',word) and not len(word) == 1
             and not '.' in word and word not in exceptions] #filter erroneous symbols
    return nltk.FreqDist(nouns)

def plot_freq_dist(book, N = 20, nouns = True, **kwargs):
    if nouns:
        fdist = noun_fdist(book, **kwargs)
        top = dict(fdist.most_common(N))
    else:
        fdist = nltk.FreqDist(token for token in book._tokens if re.search('[a-zA-Z]',token))
        top = dict(fdist.most_common(N))
    
    fig = plt.figure()
    plt.bar(np.arange(N), sorted(top.values(), reverse = True))
    labels = sorted(top.keys(), key = lambda x: top[x], reverse = True)
    from sys import version_info
    offset = 0.5 if version_info[0] < 3 else 0.3 # Graphical depiction dependent on Python version
    plt.xticks(np.arange(offset, offset + N), labels)
    plt.title('Frequency plot of the {} most common {}'.format(N, 'nouns' if nouns else 'words'))
    fig.autofmt_xdate()
    fig.show()
    
def plot_network_graph(book, N = 20, **kwargs):
    fdist = noun_fdist(book, **kwargs)
    top = dict(fdist.most_common(N))
    labels = list(top.keys())
    
    G = nx.Graph()
    G.add_nodes_from(labels)
    
    fig = plt.figure()
    nx.draw(G)
    nx.draw_networkx_labels(G, pos = nx.spring_layout(G))
    fig.show()