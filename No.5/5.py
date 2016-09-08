#!/usr/bin/env python
# coding=utf8
# __Author__ = 'Luffin'

import pickle

with open('banner.p', 'r') as f:
    P = pickle.load(f)

for x in P:
    for y in x:
        print y[0] * (y[1] - 1),
    print
