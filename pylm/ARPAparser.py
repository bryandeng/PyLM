#!/usr/bin/env python3


def read_arpa(arpa_file):
    """
    Construct a standard prob_dict from ARPA file.
    Also return the order of the model (highest n of n-grams in
    the file).
    """
    arpa_dict = {}

    with open(arpa_file, 'r') as f:
        for line in f:
            if line.rstrip() and not line.startswith('\\'):
                if line.startswith('ngram '):
                    model_order = int(line[6])
                else:
                    entry = line.rstrip().split('\t')
                    if len(entry) == 3:
                        arpa_dict[entry[1]] = (float(entry[0]),
                                               float(entry[2]))
                    else:
                        arpa_dict[entry[1]] = (float(entry[0]), )

    return arpa_dict, model_order
