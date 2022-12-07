#!/usr/bin/python3

import sys

for line in sys.stdin:
    utriples = line.split()
    u = utriples[0]
    triples = utriples[1:]
    for triple in triples:
        i, j, q1, q2, q3 = tuple(triple.split(','))
        print('%s,%s\t%s,%s,%s' % (i, j, q1, q2, q3))
    
    