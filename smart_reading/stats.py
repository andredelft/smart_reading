import nltk
from matplotlib import pyplot as plt
import numpy as np
import networkx as nx

def noun_fdist(book, treshold = 0.2):
    nouns = []
    for child in book.entities:
        if type(child) == nltk.tree.Tree:
            nouns.append(' '.join(name.capitalize() for name,tag in child))
            #nouns.append(' '.join(name.capitalize() if regex.search('NN',tag) else name.lower() for name,tag in child))
        elif type(child) == tuple:
            if 'NN' in child[1]:
                nouns.append(child[0].capitalize())
    return nltk.FreqDist(nouns)

def plot_most_common(book, N = 20, nouns = True):
    if nouns:
        fdist = noun_fdist(book)
        top = dict(fdist.most_common(N))
    else:
        fdist = nltk.FreqDist(book.raw)
        top = dict(fdist.most_common(N))

    fig = plt.figure()
    plt.bar(np.arange(N), list(top.values()))
    plt.xticks(np.arange(0.3, N + 0.3), list(top.keys()))
    plt.title('Frequency plot of the {} most common {}'.format(N, 'nouns' if nouns else 'words'))
    fig.autofmt_xdate()
    fig.show()
    
def network_graph(book, N = 20):
    fdist = noun_fdist(book)
    top = dict(fdist.most_common(N))
    labels = list(top.keys())
    
    G = nx.Graph()
    G.add_nodes_from(labels)
    
    nx.draw(G)
    nx.draw_networkx_labels(G, pos = nx.spring_layout(G))
    plt.show()