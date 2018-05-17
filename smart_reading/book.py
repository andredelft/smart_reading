import nltk
from os import path,remove
import re
from sys import version_info
if version_info[0] < 3:
    from io import open
try:
    import textract
except:
    print('\nWarning: Module \'textract\' not found on system. Will continue\n'
          'with limited support, only for .txt files and raw strings.\n'
          'Please install textract for full functionality.\n')

class Book:
    
    def __init__(self, filename, stemmer = nltk.PorterStemmer()):
        try:
            self._raw = textract.process(filename).decode('utf-8')
        except NameError as error:
            if filename.endswith('.txt'):
                with open(filename) as f:
                    self._raw = f.read()
            elif error.args[0] == "name 'textract' is not defined":
                raise TypeError('Extension {} not supported.'.format(path.splitext(filename)[1]))
            else:
                raise error
            
        self.path,self.file = path.split(filename)
        self.tokens = nltk.word_tokenize(self._raw)
        self.Text = nltk.Text(self.tokens)
        
        self.sents = [re.sub('\s+',' ',sent) for sent in nltk.sent_tokenize(self._raw)] # normalized whitespaces
        self._tags = nltk.pos_tag(self.tokens)
        
        if version_info[0] >= 3:
            # entity recognition only available for python 3 due to limited UTF-8 support of nltk.chunk.ne_chunk in python 2.7
            self.entities = nltk.chunk.ne_chunk(self._tags)
            #self._NE = [child for child in self.entities if type(child) == nltk.tree.Tree]

        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i) for (i, word) in enumerate(self.tokens))
        
        print('Succesfully loaded \'{}\' as an e-book\nTotal n.o. tokens: {}'.format(self.file,len(self.tokens)))

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
                    lcontext = ' '.join(self.tokens[i-wc:i])
                    rcontext = ' '.join(self.tokens[i:i+wc])
                    ldisplay = u'{:>{width}}'.format(lcontext[-width:], width=width)
                    rdisplay = u'{:{width}}'.format(rcontext[:width], width=width)
                    print(u'{} {}'.format(ldisplay, rdisplay))
            else:
                print('no matches')
        else:
            display_lines = len([token for token in book._tokens if token.lower() == word.lower()]) if display_all else lines
            self.Text.concordance(word, lines = display_lines, width = 2 * width)
        
def sample(type = 'txt', **kwargs):
    here = path.abspath(path.dirname(__file__))
    if type in ['txt','.txt']:
        return Book(path.join(here,'samples','Benn_Ch_II_The_Metaphysicians.txt'), **kwargs) # Downloaded from Project Gutenberg
    elif type in ['pdf','.pdf']:
        return Book(path.join(here,'samples','PhysRev.47.777.pdf'), **kwargs)
    elif type in ['epub','.epub']:
        return Book(path.join(here,'samples','Galileo_The_Sidereal_Messenger.epub'), **kwargs) # Downloaded from Project Gutenberg
    else:
        print('\nNo sample available for document type \'{}\'\n'.format(type))

def fromstring(text, title = 'text_input', **kwargs):
    filename = '{}.txt'.format(title)
    with open(filename,'w') as f:
        f.write(text)
    bk = Book('{}.txt'.format(title), **kwargs)
    remove('{}.txt'.format(title))
    return bk

def load(filename, **kwargs):
    return Book(filename, **kwargs)
