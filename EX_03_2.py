#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time

a = ('  wwwwwwww  \n')
b = (' ww      ww \n')
c = ('ww        ww\n')
d = ('ww        ww\n')
e = ('ww    ww  ww\n')
f = ('ww     ww ww\n')
g = (' ww      ww \n')
h = ('  wwwwwww ww\n')

i = ('w  w      ww\n')
j = ('w ww      ww\n')
k = ('w w       ww\n')
l = (' w        ww\n')
m = ('ww       ww \n')
n = ('w wwwwwwww  \n')

o = ('ww wwwwwww  \n')
p = (' ww      ww \n')
q = ('ww ww     ww\n')
r = ('ww  ww    ww\n')

QW=[a+b+c+d*5+e+f+g+h,a+b+c*4+i+j+k+l+m+n,o+p+q+r+d*5+c+b+a]
OSName = os.name
for i in range(13):  #旋转，跳跃，你闭着眼。
    if str(OSName) == 'nt':  # 清屏
        os.system('cls')
    elif str(OSName) == 'posix':
        os.system('clear')

    if i % 4 ==0 :
        print(QW[0])
    elif i % 4 ==1 :
        print(QW[1])
    elif i % 4 ==2 :
         print(QW[2])
    else:
         print(QW[1])

    time.sleep(1)
