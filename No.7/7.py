#!/usr/bin/env python
# coding=utf8
# __Author__ = 'Luffin'


# 图片中有一条马赛克一样的线，里面肯定有数据
# 使用如QQ截图等工具自带的测量工具计算出线条的宽608，长8，线其实坐标(0, 43)，线条中每个方块间距7，且颜色一样
# 将图片转换灰度
# 以间距7，提取每个快的像素值，即ASCII码
# 转换为文字


from PIL import Image

im = Image.open('oxygen.png').convert('L')

print ''.join([chr(im.getpixel((i, 43))) for i in xrange(0, 609, 7)])

l = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join([chr(i) for i in l])
