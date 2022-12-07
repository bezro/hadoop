#!/usr/bin/python3

import sys

prev_u = ''
first_line = True
strings = []
seen_items = set()

for line in sys.stdin:
    u, string = line.split(maxsplit=1)

    if first_line:
        prev_u = u

    if u == prev_u:
        if string[0] == 'w':
            r, name = string[1:].split(',', maxsplit=1)
            strings.append('%.3f,%s' % (9.999 - float(r), name))
        else:
            seen_items.add(string[1:])
        
    else:
        strings_2 = []
        for x in strings:
            a, b = x.split(',', maxsplit=1)
            if b not in seen_items:
                strings_2.append(x)
        if len(strings_2):
            print('%d' % int(prev_u), end='')
        strings_2.sort()
        for s in strings_2[:100]:
            r, name = s.split(',', maxsplit=1)
            print('@%.3f%%%s' % (9.999 - float(r), name[:-1]), end='')
        if len(strings_2):
            print()

        strings = []
        seen_items = set()
        if string[0] == 'w':
            r, name = string[1:].split(',', maxsplit=1)                
            strings.append('%.3f,%s' % (9.999 - float(r), name))
        else:
            seen_items.add(string[1:])
        prev_u = u

    first_line = False


strings_2 = []
for x in strings:
    a, b = x.split(',', maxsplit=1)
    if b not in seen_items:
        strings_2.append(x)
if len(strings_2):
    print('%d' % int(u), end='')
strings_2.sort()
for s in strings_2[:100]:
    r, name = s.split(',', maxsplit=1)
    print('@%.3f%%%s' % (9.999 - float(r), name[:-1]), end='')
if len(strings_2):
    print()
