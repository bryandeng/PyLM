#!/usr/bin/env python3

from .misc import tokens2str


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
        matched -= 1
        history = tokens2str(n_gram_bo[:-1])
        if prob_dict.get(history) is not None:
            prob += prob_dict.get(history)[1]  # back-off
        n_gram_bo.pop(0)
    else:
        prob += prob_dict[tokens2str(n_gram_bo)][0]

    return prob, matched
