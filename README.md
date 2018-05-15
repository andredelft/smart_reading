# Smart Reading

## About

Smart Reading is a Python module designed for increasing the understanding of various textsforms by using natural language processing. It is heavily based on tools available from the [Natural Language Toolkit](https://www.nltk.org) (NLTK).

### Installation

The smart_reading module is available for Python 2.7+, but recommended to run on Python 3+ for a more thorough unicode support. Install via pip (or any other desired client)

```
$ pip install smart_reading
```

or by downloading the source on [PyPI](https://pypi.org/project/smart-reading/) or [GitHub](https://github.com/andredelft/smart_reading) and running in the root folder:

```
$ python setup.py install
```

## Functionality

Three sample texts are included, and callable via the function `smart_reading.book.sample`:

```python
>>> import smart_reading as sr
>>> sr.book.sample() # or sr.book.sample('txt')

Succesfully loaded 'Benn_Ch_II_The_Metaphysicians.txt' as an e-book
Total n.o. tokens: 10420

<smart_reading.book.Book instance at 0x105a546c8>
>>> sr.book.sample('pdf')

Succesfully loaded 'PhysRev.47.777.pdf' as an e-book
Total n.o. tokens: 3192

<smart_reading.book.Book instance at 0x110c0ebd8>
>>> sr.book.sample('epub')

Succesfully loaded 'Mason_Throwing_Sticks.epub' as an e-book
Total n.o. tokens: 13581

<smart_reading.book.Book instance at 0x105a46e60>
>>> 

```