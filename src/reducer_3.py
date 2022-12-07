#!/usr/bin/python3

import sys

prev_j = ''
first_line = True
i_s = []
u_s = []
s_s = []
r_s = []

for line in sys.stdin:
    j, other = line.split()
    sign_1, sign_2, ind = other.split(',')

    if first_line:
        prev_j = j

    if j == prev_j:
        if ind == 's':
            # Если строка пришла из матрицы сходств, то запоминаем товар и sim(i,j)
            i_s.append(int(sign_1))
            s_s.append(float(sign_2))
        else:
            # Если строка пришла из списка рейтингов, то запоминаем пользователя и рейтинг
            u_s.append(int(sign_1))
            r_s.append(float(sign_2))
    else:
        for i, s in zip(i_s, s_s):
            for u, r in zip(u_s, r_s):
                print('%06d,%03d\t%.3f,%.3f' % (i, u, r*s, s))

        if ind == 's':
            i_s = [int(sign_1)]
            s_s = [float(sign_2)]
            u_s = []
            r_s = []
        else:
            i_s = []
            s_s = []
            u_s = [int(sign_1)]
            r_s = [float(sign_2)]
        prev_j = j

    first_line = False

for i, s in zip(i_s, s_s):
    for u, r in zip(u_s, r_s):
        print('%06d,%03d\t%.3f,%.3f' % (i, u, r*s, s))