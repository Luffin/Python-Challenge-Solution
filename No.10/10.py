#!/usr/bin/env python
# coding=utf8
# __Author__ = 'Luffin'

# 规律没想出来
# 搜索得到规律，统计前一个字符串里字符的个数
# 1, 11, 21, 1211, 111221
# 11: 前一个数有1个1
# 21: 前一个数有2个1
# 1211: 前一个数有1个2,1个1
# 111221: 前一个数有1个1,1个2,2个1

# 利用re里的finditerp匹配所有非重叠字符串

import re


def creatNum(num):
    return ''.join([str(len(m.group())) + m.group()[0] for m in re.finditer(r'(\d)\1*', num)])


num = '1'
for i in xrange(1, 31):
    num = creatNum(num)
print len(num)
