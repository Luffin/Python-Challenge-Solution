#!/usr/bin/env python
# coding=utf8
# __Author__ = 'Luffin'
import urllib2
import re

m = '12345'
count = 1
while m:
    if m == '16044':
        m = str(int(m) / 2)
    print count, m
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    try:
        content = urllib2.urlopen(url + m, timeout=5).read()
    except Exception:
        continue
    try:
        m = re.findall('\d{1,}', content)[-1]
    except Exception:
        break
    count += 1
print content
