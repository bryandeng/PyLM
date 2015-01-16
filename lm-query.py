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

# assign dummy ids to words in vocab, reserve "0" for OOVs
word_ids = {word: index+1 for index, word in enumerate(vocab)}

results = []

for line in sys.stdin:
    results_per_sentence = []

    words_original = pylm.tokenize(line)
    words, oov_count = pylm.handle_oov(words_original, vocab)

    for index, word in list(enumerate(words))[1:]:
        n_gram = words[max(0, index-model_order+1):index+1]
        prob, matched_len = pylm.prob_backoff(n_gram, arpa_dict)
        results_per_sentence.append(
            (words_original[index], word_ids.get(words_original[index], 0),
             matched_len, prob)
            )

    results_per_sentence.append(oov_count)
    results.append(results_per_sentence)

pylm.kenlm_output(results)
