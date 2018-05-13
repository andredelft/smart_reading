import nltk as nltk
from os import path,remove
import re

class Book:
    
    def __init__(self, filename, stemmer = nltk.PorterStemmer()):
        if filename.endswith('.txt'):
            with open(filename) as f:
                self._raw = f.read()
            self._path,self.title = path.split(filename)
            self.title = path.splitext(self.title)[0]
            self._tokens = nltk.word_tokenize(self._raw)
            self.Text = nltk.Text(self._tokens)
            
            self._sents = [re.sub('\s+',' ',sent) for sent in nltk.sent_tokenize(self._raw)] # normalized whitespaces
            self._tags = nltk.pos_tag(self._tokens)
            self.entities = nltk.chunk.ne_chunk(self._tags)
            self._NE = [child for child in self.entities if type(child) == nltk.tree.Tree]

            self._stemmer = stemmer
            self._index = nltk.Index((self._stem(word), i) for (i, word) in enumerate(self._tokens))
            
            print("Succesfully loaded {} as an e-book".format(self.title),
                  "Total n.o. tokens: {}".format(len(self._tokens)), sep = '\n')
        else:
            raise TypeError('Extension {} not supported.'.format(path.splitext(filename)[1]))

    def _stem(self, word):
        return self._stemmer.stem(word).lower()
 
    def concordance(self, word, inflections = True, lines = 25, width = 40, display_all = False):
        if inflections:
            # Inspired from ex. 3.6 of the NLTK book
            # http://www.nltk.org/book/ch03.htm, retrieved at 05-13-18
            key = self._stem(word)
            wc = width//4  # words of context
            locs = self._index[key]
            no_locs = len(locs)
            if no_locs > 0:
                display_lines = no_locs if display_all else min(no_locs,lines)
                print('Displaying {} of {} matches:'.format(display_lines,no_locs))
                for i in self._index[key][:display_lines]:
                    lcontext = ' '.join(self._tokens[i-wc:i])
                    rcontext = ' '.join(self._tokens[i:i+wc])
                    ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
                    rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
                    print(ldisplay, rdisplay)
            else:
                print('no matches')
        else:
            display_lines = len([token for token in book._tokens if token.lower() == word.lower()]) if display_all else lines
            self.Text.concordance(word, lines = display_lines, width = 2 * width)
        
def sample():
    return Book(path.join(path.abspath(path.dirname(__file__)),'Benn_ch_II.txt'))

def fromstring(text, title = 'text_input'):
    filename = '{}.txt'.format(title)
    with open(filename,'w') as f:
        f.write(text)
    bk = Book('{}.txt'.format(title))
    remove('{}.txt'.format(title))
    return bk

#def load(filename):
#    ext = path.splitext()
        