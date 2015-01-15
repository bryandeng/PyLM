#!/usr/bin/env python3

import re


def ngrams(words, n):
    return [words[i:i+n] for i in range(len(words)-n+1)]


def tokenize(sequence):
    words = re.findall(r"[\w']+|[.,!?;]", sequence)
    words.insert(0, '<s>')
    words.append('</s>')
    return words


def tokens2str(words):
    return ' '.join(words)


def prob_backoff(n_gram, prob_dict):
    """
    Return probability and length of n-gram match from back-off model.

    Input:
    n_gram: a Python list of words in the n gram.
    prob_dict: standard prob_dict.
    """
    n_gram_bo = n_gram.copy()
    prob = 0
    matched = len(n_gram)

    while (prob_dict.get(tokens2str(n_gram_bo)) is None):
        n_gram_bo.pop(0)
        matched -= 1
        prob += prob_dict[tokens2str(n_gram_bo)][1]  # back-off
    else:
        prob += prob_dict[tokens2str(n_gram_bo)][0]

    return prob, matched
