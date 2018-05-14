from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name = 'smart_reading',
    version = '0.3.2',
    description = 'An NLTK-based toolkit aimed at increasing the understanding of various texts.',
    url = 'https://github.com/andredelft/smart_reading',
    packages = find_packages(),
    install_requires = ['nltk','networkx','numpy','matplotlib'],
    keywords = 'ebook understanding nltk reading toolkit',
    long_description = long_description,
    include_package_data = True,
    python_requires = '>=2.7',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ]
)