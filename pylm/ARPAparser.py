#!/usr/bin/env python3

'''
The script converts arpa file into dict structure.
'''

import sys


def read_arpa(arpafile):
    '''This function reads the arpa file and returns its dict representation'''
    with open(arpafile, 'r') as f:
        fdata = f.read()

    arpa_lines = [l for l in fdata.splitlines() if len(l.split()) > 2]
    arpa_dict = [dict({l.split()[1]: (l.split()[0], l.split()[2])})
                 for l in arpa_lines]
    return arpa_dict


if __name__ == '__main__':
    read_arpa(sys.argv[1])

