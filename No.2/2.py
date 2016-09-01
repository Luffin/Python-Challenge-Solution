#!/usr/bin/env python
# coding=utf8
# __Author__ = 'Luffin'
import re
import urllib

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
content = urllib.urlopen(url).read()
m = re.findall('-->[\s\S]*<!--([\s\S]*)-->', content)
mess_text = m[0].replace('\n', '')

done = []
res = ''
for c in mess_text:
    if c in done:
        continue
    if mess_text.count(c) < 10:
        res += c
    done.append(c)

print res
