#!/usr/bin/env python3

import math
import sys


def kenlm_output(results):
    """
    Format and print query results in the same way as KenLM.
    """
    oov_count_total = 0
    tokens_count = 0
    pp_incl_oovs, pp_excl_oovs = [], []

    for result_per_sentence in results:
        oov_count_total += result_per_sentence[-1]
        total = 0

        for result in result_per_sentence[:-1]:
            word, id_, matched_len, prob = (result[0], result[1], result[2],
                                            result[3])
            print(word + '=' + str(id_), matched_len,
                  round(prob, 5), end='\t')

            total += prob
            tokens_count += 1
            pp_incl_oovs.append(prob)
            if id_ is not 0:
                pp_excl_oovs.append(prob)

        print('Total:', round(total, 5), end=' ')
        print('OOV:', result_per_sentence[-1])

    pp_incl_oovs = math.pow(10, -sum(pp_incl_oovs) / len(pp_incl_oovs))
    pp_excl_oovs = math.pow(10, -sum(pp_excl_oovs) / len(pp_excl_oovs))

    print('Perplexity including OOVs:', round(pp_incl_oovs, 3), sep='\t',
          file=sys.stderr)
    print('Perplexity excluding OOVs:', round(pp_excl_oovs, 3), sep='\t',
          file=sys.stderr)

    print('OOVs:', oov_count_total, sep='\t')
    print('Tokens:', tokens_count, sep='\t')
