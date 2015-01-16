#!/usr/bin/env python3

import re


def ngrams(words, n):
    return [words[i:i+n] for i in range(len(words)-n+1)]


def tokenize(string, punc=False):
    if punc:
        words = re.findall(r"[\w']+|[.,!?;]", string)
    else:
        words = string.split()
    words.insert(0, '<s>')
    words.append('</s>')
    return words


def tokens2str(words):
    return ' '.join(words)


def handle_oov(words, vocabulary):
    return [word if word in vocabulary else '<unk>' for word in words]
