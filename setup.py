from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name = 'smart_reading',
    version = '1.1.3',
    description = 'An NLTK-based toolkit aimed at increasing the understanding of various texts.',
    url = 'https://github.com/andredelft/smart_reading',
    packages = find_packages(),
    install_requires = ['nltk','networkx','numpy','matplotlib'],
    keywords = 'ebook understanding nltk reading toolkit',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    include_package_data = True,
    python_requires = '>=2.7',
    author = 'Andre van Delft',
    author_email = 'andrevandelft@outlook.com',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)