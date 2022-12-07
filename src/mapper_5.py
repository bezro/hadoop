#!/usr/bin/python3

import sys, csv

movies = csv.reader(open('movies.csv', 'r'))
names = dict()
for id, title, _ in movies:
    if id[0].isdigit():
        names[int(id)] = title

for line in sys.stdin:
    if not line[0].isdigit():
        continue
    if '\t' in line:
        iu, r = line.split()
        i, u = iu.split(',')
        print('%s\tw%s,%s' % (u, r, names[int(i)]))
    else:
        u, i, r, _ = line.split(',')
        print('%s\tu%s' % (u, names[int(i)]))
