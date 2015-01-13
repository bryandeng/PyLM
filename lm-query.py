#!/usr/bin/env python3

import argparse
import os
import shelve
import sys

import pylm

parser = argparse.ArgumentParser(
    description='language model querying software')
parser.add_argument('arpa_file', help='path to ARPA file')
parser.add_argument('--version', action='version', version='0.1a')
args = parser.parse_args()

arpa_file = args.arpa_file
arpa_dict_filename = arpa_file + '.dict'
if not os.path.exists(arpa_file):
    parser.error('no such ARPA file.')

if os.path.exists(arpa_dict_filename):
    with shelve.open(arpa_dict_filename, 'r') as db:
        arpa_dict, max_n = db['arpa_dict'], db['max_n']
else:
    arpa_dict, max_n = pylm.read_arpa(arpa_file)
    with shelve.open(arpa_dict_filename, 'c') as db:
        db['arpa_dict'] = arpa_dict
        db['max_n'] = max_n

for line in sys.stdin:
    for ngram in pylm.ngrams(line, max_n):
        ngram_str = ' '.join(ngram)
        print(ngram_str, arpa_dict.get(ngram_str))
