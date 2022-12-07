#!/usr/bin/python3

# ratings.csv -----> mapper_1.py

import sys

for line in sys.stdin:
    if not line[0].isdigit():
        continue

    u, i, r, _ = tuple(line.split(','))
    print('%03d\t%s,%.3f' % (int(u), i, float(r) / 5))
