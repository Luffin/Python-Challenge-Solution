#!/usr/bin/env python
# coding=utf8
# __Author__ = 'Luffin'

import re
import zipfile

with zipfile.ZipFile('channel.zip', 'r') as zf:
    filenum = len(zf.namelist())
    name = '90052'
    suffix = '.txt'
    i = 0
    res = ''
    while i < filenum:
        content = zf.read(name + suffix)
        m = re.search('\d{1,5}', content)
        if m:
            print m.group()
            res += zf.getinfo(name + suffix).comment
            name = m.group()
        else:
            break
        i += 1
print res
