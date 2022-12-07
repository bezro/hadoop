#!/usr/bin/python3

import sys

from math import sqrt

EPS = 1e-8

def sat(x: float):
    if x > 1:
        return 1.0
    if x < -1:
        return -1.0
    return x

prev_ij = ''
first_line = True
summa_mul = 0.
summa_sqr_1 = 0.
summa_sqr_2 = 0.

for line in sys.stdin:
    ij, q = tuple(line.split())
    q1, q2, q3 = q.split(',')

    if first_line:
        prev_ij = ij

    if ij == prev_ij:
        summa_mul += float(q1)
        summa_sqr_1 += float(q2)
        summa_sqr_2 += float(q3)
    else:
        result = sat(summa_mul / (sqrt(summa_sqr_1 * summa_sqr_2) + EPS))
        if result > 0:
            print('%s\t%.3f' % (prev_ij, result))
        prev_ij = ij
        summa_mul = float(q1)
        summa_sqr_1 = float(q2)
        summa_sqr_2 = float(q3)

    first_line = False
result = sat(summa_mul / (sqrt(summa_sqr_1 * summa_sqr_2) + EPS))
if result > 0:
    print('%s\t%.3f' % (ij, result))

