#!/usr/bin/env python
# coding=utf8
# __Author__ = 'Luffin'
from string import lowercase, maketrans

c = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
to = lowercase[2:] + lowercase[:2]
table = maketrans(lowercase, to)

print c.translate(table)
