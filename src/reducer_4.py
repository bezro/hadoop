#!/usr/bin/python3

import sys

EPS = 1e-8

prev_ju = ''
first_line = True
summa_rs = 0.
summa_s = 0.

for line in sys.stdin:
    ju, rss = tuple(line.split())
    rs, s = rss.split(',')

    if first_line:
        prev_ju = ju

    if ju == prev_ju:
        summa_rs += float(rs)
        summa_s += float(s)
    else:
        result = summa_rs / (summa_s + EPS)
        print('%s\t%.3f' % (prev_ju, result))
        prev_ju = ju
        summa_rs = float(rs)
        summa_s = float(s)

    first_line = False
result = summa_rs / (summa_s + EPS)
print('%s\t%.3f' % (ju, result))

