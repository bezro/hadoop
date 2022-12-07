#!/usr/bin/python3

import sys

for line in sys.stdin:
    # Предыдущая стадия
    if '\t' in line:
        ij, sim = tuple(line.split())
        i, j = tuple(ij.split(','))
        print('%06d\t%06d,%.3f,s' % (int(j), int(i), float(sim)))

    # 
    else:
        if not line[0].isdigit():
            continue
        u, j, r, _ = tuple(line.split(','))
        print('%06d\t%03d,%.3f,r' % (int(j), int(u), float(r) / 5))
