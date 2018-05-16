# Smart Reading

## About

`smart_Reading` is a Python module designed for increasing the understanding of various textforms by using natural language processing. It is heavily based on tools available from the [Natural Language Toolkit](https://www.nltk.org) (NLTK), which are used in various applications and provided with extensions.

### Installation

The module is available for Python 2.7+, but recommended to run on Python 3+ for a more thorough unicode support and prettier graphs. Install via pip (or any other desired client):
```
$ pip install smart_reading
```
or by downloading the source code on [PyPI](https://pypi.org/project/smart-reading/) or [GitHub](https://github.com/andredelft/smart_reading) and running the following command in the root folder:
```
$ python setup.py install
```
## Importing texts

The basic functionality of `smart_reading` is to import a given textfile into a `smart_reading.book.Book` object, which can be used to perform several developed analyses. Textfiles can be imported via the function `smart_reading.book.load(filename)`. This function utilizes the functionality of the module `textract` to extract textual information of almost any given data structure, including .txt, .pdf, .epub and .docx. See the [online manual](https://textract.readthedocs.io/en/stable/) for more details on the inner workings of this module. When this module is not found on the system, the program continues with a limited functionality, in which only .txt files can be read. This limited functionality is added because it is experienced that the installation of `textract` does not always succeed. The user that is not able to install `textract` but does want to import other text formats is encouraged to build alternative pipelines to extract text into a .txt file, which in turn can be imported in the `smart_reading.book.load` function.

Additionally, a given string can be imported as an e-book via `smart_reading.book.fromstring(text)`.

Three sample texts are included with different file structures, callable via the function `smart_reading.book.sample`:

```pycon
>>> import smart_reading as sr
>>> sr.book.sample() # or sr.book.sample('txt')
Succesfully loaded 'Benn_Ch_II_The_Metaphysicians.txt' as an e-book
Total n.o. tokens: 10420
<smart_reading.book.Book instance at 0x105a546c8>
>>> sr.book.sample('pdf')
Succesfully loaded 'PhysRev.47.777.pdf' as an e-book
Total n.o. tokens: 3192
<smart_reading.book.Book instance at 0x110c0ebd8>
>>> sr.book.sample('epub') # this one takes a while to load
Succesfully loaded 'Galileo_The_Sidereal_Messenger.epub' as an e-book
Total n.o. tokens: 40372
<smart_reading.book.Book instance at 0x105a46e60>
```

## Functionality

As mentioned, the given text are imported into a `smart_reading.book.Book` type object. The different tools that this object provides are listed below.

### Concordance

A concordance is developed as an extension of the `nltk.text.Text.concordance` function, which incorporates [example 3.6](http://www.nltk.org/book/ch03.html#code-stemmer-indexing) of the NLTK manual, such that it not only matches with exact copies of a given word, but also inflections:

```pycon
>>> import smart_reading as sr
>>> bk = sr.book.sample()
Succesfully loaded 'Benn_Ch_II_The_Metaphysicians.txt' as an e-book
Total n.o. tokens: 10420
>>> bk.concordance('philosopher')
Displaying 17 of 17 matches:
nce of an independent income enabled the philosopher to live where he liked ; and
by our opinion of his metaphysics . As a philosopher Descartes has , to begin wit
r dazzle ; they could not convince . The philosophers professed to teach truth ; 
inctly are all true . In his other great philosophical work , the _Meditations_ ,
o his postulate of universal doubt , our philosopher argues from this to an imper
Here he agrees with another mathematical philosopher , Plato , who says the same 
at least one astronomer , who was also a philosopher , declared that the ultimate
 personality of God . SPINOZA . With the philosopher whom I have just named we co
sion of 500 florins on Spinoza , but the philosopher would accept no more than 30
l . To appreciate the work of the Hebrew philosopher , of the lonely muser , bred
 divine substance . In fact , the Hebrew philosopher does this , declaring boldly
peppers his pages . Yet , like the Greek philosophers , he is much more modern , 
 name of his great work that for him the philosophical problem is essentially a p
 . But he parts company with the English philosopher in his theory of what it mea
 alone , however , does not make a great philosopher ; character also is required
rity than any one utterance of any other philosopher ; but that fame is due to th
 work . On _à priori_ grounds the German philosopher seems to have an incontrover
```

In order to deal with inflections, the stemmer `nltk.PorterStemmer` is used by default. Other stemmers can be sent through the keyword *stemmer* when importing a textfile.

### `nltk.text.Text` attribute

A `smart_reading.book.Book` object contains an attribute `Text`, which is an `nltk.text.Text` type object and as such includes all its attributes as developed by NLTK. These include finding collocations, similar words, and creating lexical disperion plots. See the [NLTK API](https://www.nltk.org/api/nltk.html#nltk.text.Text) for its full documentation

```pycon
>>> bk.Text.collocations()
fullest extent; infinite Power; material world; Princess Elizabeth;
external world; paramount object; supernatural revelation; two
attributes; necessarily exist; Queen Christina; early age; whole
universe; final causes; mathematical demonstration; metaphysical
system; perfection involves; best possible; many distinct;
mathematical method; divine substance
>>> bk.Text.dispersion_plot(['Descartes','Malebranche','Spinoza','Leibniz'])
```
![alt text](https://i.imgur.com/TgGu656.png "Lexical Dispersion Plot")

### The `smart_reading.stats` submodule

The `smart_reading` module comes with a `stats` submodule, which uses `matplotlib.pyplot` to create the several types of graps out of a given `smart_reading.book.Book` object, callable via the following functions:

#### smart_reading.stats.plot_noun_hist(book, no_nouns = 20, named_entities = True, exceptions = [], **kwargs)

Create a histogram of the most common nouns appearing in given text.
* *no_nouns*: Number of nouns that will be included in the graph (i.e. number of bars).
* *named_entities*: If false, this will exclude named entities like people and places that are recognized by the `nltk.chunk.ne_chunk` routine. This option is not supported in versions of Python 2.
* *exceptions*: An iterable of nouns that will be excluded from the analysis
* Further keyword arguments are passed to `matplotlib.pyplot.fig`.

```pycon
>>> bk2 = sr.book.sample('pdf')
Succesfully loaded 'PhysRev.47.777.pdf' as an e-book
Total n.o. tokens: 3192
>>> sr.stats.plot_noun_dist(bk2)
```
![alt text](https://imgur.com/fRlb1aw.png "Frequency Plot")

#### smart_reading.stats.plot_network_graph(book, no_nouns = 10, treshold = 3, exclude_empty = True, named_entities = True, exceptions = [], **kwargs)

Create a network graph using the module `neworkx` which depicts the relationship between frequently appearing graphs. The nouns appear as nodes, and edges are drawn between nouns if they appear frequently in the same sentences. A [temperature color scheme](https://en.wikipedia.org/wiki/Color_temperature) is used on the edges to depict the frequency in which nouns appear together (red = very often, blue = a few times).
* *no_nouns*: Number of nouns that will be included in the graph (i.e. number of nodes). Can become less in the final result if *exclude_empty* is true, see below.
* *treshold*: The minimal number of sentences in which two given nouns have to appear in order for an edge to be drawn. Can be used to simplify graphs with a lot of edges.
* *exclude_empty*: if True, this will exclude the nodes from the graph that do not have edges. Note that this will reduce the number of nouns depicted, as declared in *no_nouns* above
* *exceptions*: an iterable of nouns that will be excluded from the analysis.
* Further keyword arguments are passed to `matplotlib.pyplot.fig`.

```pycon
>>> sr.stats.plot_network_graph(bk2)
```
![alt text](https://imgur.com/pRA0yy2.png "Network Graph")
```pycon
>>> bk3 = sr.book.sample('epub')
Succesfully loaded 'Galileo_The_Sidereal_Messenger.epub' as an e-book
Total n.o. tokens: 40372
>>> sr.stats.plot_network_graph(bk3, exceptions = ['Galileo'], treshold = 10)
```
![alt text](https://imgur.com/NdG4vIs.png "Network Graph")