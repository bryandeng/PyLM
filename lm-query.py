#!/usr/bin/env python3

import argparse
import os
import sys

import pylm

parser = argparse.ArgumentParser(
    description='language model querying software')
parser.add_argument('arpa_file', help='path to ARPA file')
parser.add_argument('--version', action='version', version='0.1a')
args = parser.parse_args()

arpa_file = args.arpa_file
if not os.path.exists(arpa_file):
    parser.error('no such ARPA file.')
else:
    arpa_dict, vocab, model_order = pylm.read_arpa(arpa_file)

for line in sys.stdin:
    words_original = pylm.tokenize(line)
    words = pylm.handle_oov(words_original, vocab)
    for index, word in list(enumerate(words))[1:]:
        n_gram = words[max(0, index-model_order+1):index+1]
        prob, matched = pylm.prob_backoff(n_gram, arpa_dict)
        print(words_original[index]+'=', matched, prob)
