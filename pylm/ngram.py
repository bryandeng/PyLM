#!/usr/bin/env python3

import re


def ngrams(sentence, n):
    token_list = re.findall(r"[\w']+|[.,!?;]", sentence)
    token_list.insert(0, '<s>')
    token_list.append('</s>')
    return [token_list[i:i+n] for i in range(len(token_list)-n+1)]