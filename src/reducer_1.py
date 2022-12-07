#!/usr/bin/python3

import sys

prev_u = -1
first_line = True
i_s = []
r_s = []

for line in sys.stdin:
    u, ir = tuple(line.split())
    i, r = tuple(ir.split(','))

    u = int(u)
    i = int(i)
    r = float(r)

    if first_line:
        prev_u = u

    if u == prev_u:
        i_s.append(i)
        r_s.append(r)
    else:
        print('%d\t' % prev_u, end='')
        mean_rating = sum(r_s) / len(r_s)
        for i1, r1 in zip(i_s, r_s):
            for i2, r2 in zip(i_s, r_s):
                print('%06d,%06d,%.3f,%.3f,%.3f ' % (i1, i2, (r1 - mean_rating)*(r2 - mean_rating), 
                    (r1 - mean_rating) ** 2, (r2 - mean_rating) ** 2), end='')
        print()
        i_s = [i]
        r_s = [r]
        prev_u = u

    first_line = False

print('%d\t' % u, end='')
mean_rating = sum(r_s) / len(r_s)
for i1, r1 in zip(i_s, r_s):
    for i2, r2 in zip(i_s, r_s):
        print('%06d,%06d,%.3f,%.3f,%.3f ' % (i1, i2, (r1 - mean_rating)*(r2 - mean_rating), 
            (r1 - mean_rating) ** 2, (r2 - mean_rating) ** 2), end='')
print()
