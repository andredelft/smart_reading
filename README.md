# Smart Reading

## About

`smart_Reading` is a Python module designed for increasing the understanding of various textsforms by using natural language processing. It is heavily based on tools available from the [Natural Language Toolkit](https://www.nltk.org) (NLTK), which are used in various applications or provided with an extension.

### Installation

The module is available for Python 2.7+, but recommended to run on Python 3+ for a more thorough unicode support (and prettier graphs). Install via pip (or any other desired client):
```
$ pip install smart_reading
```
or by downloading the source code on [PyPI](https://pypi.org/project/smart-reading/) or [GitHub](https://github.com/andredelft/smart_reading) and running the following command in the root folder:
```
$ python setup.py install
```
## Usage

### Importing texts

The basic functionality of `smart_reading` is to provide the user with an analysis of any given text. Textfiles can be imported via the function `smart_reading.book.load(filename)`. This function utilizes the functionality of the module `textract` to extract textual information of almost any given data form, including .txt, .pdf, .epub, .docx etc. See the [online manual](https://textract.readthedocs.io/en/stable/) for more details on the inner workings of this module. When this module is not found on the system, the program continues with a limited functionality, in which only .txt files can be read. Additionally, a given string can be imported as an e-book via `smart_reading.book.fromstring(text)`.

Three sample texts are also included with different file structures, and available via the function `smart_reading.book.sample`:
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
```
### Functionality

TBD