# PyLM

## What is it
**PyLM** aims to be a full-featured language model package for Python. It deals with [**language models**](http://en.wikipedia.org/wiki/Language_model), which are basically probability distributions of sequences of words.

## Main Features
Now available:

  - Import n-gram models from ARPA files
  - A simple language model querying script called `lm-query.py`

Planned:

  - Uniform interface for language models like n-grams (including back-off), topic-based language models, etc.
  - Wrapper for other toolkits like [RNNLM](http://rnnlm.org/) and [word2vec](https://code.google.com/p/word2vec/).

## Installation
The source code is currently hosted on GitHub at:
https://github.com/bryandeng/PyLM

Just clone this repo:

```
git clone https://github.com/bryandeng/PyLM
```

For now you don't need to install it. Go into its directory and have a try.

## Command-line Usage:
You can play with `lm-query.py` like this:

```
./lm-query.py lm.arpa < test.txt > test.probs 2> test.pp
```

`lm-query.py` calculates the probabilities of words in different sentences in `test.txt` and writes results in the same format as [KenLM](https://kheafield.com/code/kenlm/) to `stdout`, also outputs perplexities to `stderr`. You can redirect outputs to files as shown above.

## Dependencies
For now it only depends on the standard installation of Python 3.

## License
GPLv3
