#!/usr/bin/env python
# coding=utf8
# __Author__ = 'Luffin'
import re
import urllib

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
content = urllib.urlopen(url).read()
m = re.findall('<!--([\s\S]*)-->', content)
mess_text = m[0].replace('\n', '')

res = re.findall('[a-z]+[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]+', mess_text)
print ''.join(res)
