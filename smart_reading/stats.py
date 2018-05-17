import nltk
from matplotlib import pyplot as plt
import numpy as np
import networkx as nx
import re
from itertools import combinations

def _noun_fdist(book, named_entities = True, exceptions = []):
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
    
    exceptions = [word.lower() for word in exceptions]
    nouns = [word for word in nouns if re.search('[a-zA-Z]',word) and len(word) != 1
             and '.' not in word and word.lower() not in exceptions] #filter erroneous symbols
    return nltk.FreqDist(nouns)

def plot_noun_hist(book, no_nouns = 20, named_entities = True, exceptions = [], **kwargs):
    fdist = _noun_fdist(book, named_entities, exceptions)
    top = dict(fdist.most_common(no_nouns))
    
    fig = plt.figure(**kwargs)
    plt.bar(np.arange(no_nouns), sorted(top.values(), reverse = True))
    labels = sorted(top.keys(), key = lambda x: top[x], reverse = True)
    from sys import version_info
    offset = 0.5 if version_info[0] < 3 else 0.3 # Graphical depiction dependent on Python version
    plt.xticks(np.arange(offset, offset + no_nouns), labels)
    plt.title('Frequency plot of the {} most common nouns'.format(no_nouns)
    fig.autofmt_xdate()
    fig.show()
    
def plot_network_graph(book, no_nouns = 10, treshold = 3, exclude_singles = True,
                       named_entities = True, exceptions = [], **kwargs):
    fdist = _noun_fdist(book, named_entities, exceptions)
    top = dict(fdist.most_common(no_nouns))
    labels = list(top.keys())
    label_pairs = list(combinations(labels,2))
    G = nx.Graph()
    if not exclude_singles:
        G.add_nodes_from(labels)
    
    # Create edges:
    dict_pairs = {pair: 0 for pair in label_pairs}
    for sent in book.sents:
        labels_in_sent = [label for label in labels if label.lower() in nltk.word_tokenize(sent.lower())]
        for pair in combinations(labels_in_sent,2):
            try:
                dict_pairs[pair] += 1
            except KeyError:
                dict_pairs[(pair[1],pair[0])] += 1
    G.add_weighted_edges_from((pair[0],pair[1],dict_pairs[pair]) for pair in label_pairs if dict_pairs[pair] >= treshold)
    
    fig = plt.figure(**kwargs)
    pos = nx.spring_layout(G)
    colors = [edge[2] for edge in G.edges.data('weight')]
    nx.draw(G, pos, with_labels=True, node_color='#A0CBE2', edge_cmap=plt.cm.coolwarm, edge_color = colors,
            font_weight='bold', node_shape = 'o', width = 3)
    fig.show()