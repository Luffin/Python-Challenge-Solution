#!/usr/bin/env python
# coding=utf8
# __Author__ = 'Luffin'

# 查看源码发现../return/good.html的网站和un及pw
# 访问good.html需要认证
# 猜测需要破解un及pw作为用户名和密码
# 搜索un的前几个字符发现为bz2格式压缩

import bz2

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print bz2.decompress(un)
print bz2.decompress(pw)
