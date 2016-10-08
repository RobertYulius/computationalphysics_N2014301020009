#Exercise_02: Print, print, print your name.


## Abstract

 - Spelling my English name with symbols or letters.
 - compare Python version 3 and 2.7 on 'print' function.
 
## Codes


### **Python 3** version

 
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#用字符画的方式<del>虚区</del>输出自己的名字，逐行打印并添加延迟。 Coding with Python 3

import time

print(' gga')
time.sleep(0.5)
print(' ggg                           eg   ae                                                                eg')
time.sleep(0.5)
print(' eaa                           ga   ')
time.sleep(0.5)
print(' aaa      ig     ea            eg   ga    ggaaega   geieaggi     aagaiea   gii   eag   aea  gieggai   gg')
time.sleep(0.5)
print(' gia      ga     gg            ge   ig         ga   ei     ei   ig     gg   ee   agg   eg  ee     ai  ai')
time.sleep(0.5)
print(' egg      gg     ai            ia   ge    egeeaii   ag     aa  gi      gg    ag ig ig ei   iggiieegi  ga')
time.sleep(0.5)
print(' aai      gg     gi           gi    ga    ai   ig   ae     ai  ag      ge    giii   egg    eg         ii')
time.sleep(0.5)
print(' iegaggi   eagggae         aaag     ig    gaeei ig  aa     eg   igegiggig     ie     ag     eigeeeg   ga')
time.sleep(0.5)
print('                                                                       ig')
time.sleep(0.5)
print('                                                               gi     ig')
time.sleep(0.5)
print('                                                                 egggeg')
time.sleep(0.5)
print('')
time.sleep(0.5)
print('')
time.sleep(1)
print('                                                                                         Made by N')

#  gga
#  ggg                           eg   ae                                                                eg
#  eaa
#  aaa      ig     ea            eg   ga    ggaaega   geieaggi     aagaiea   gii   eag   aea  gieggai   gg
#  gia      ga     gg            ge   ig         ga   ei     ei   ig     gg   ee   agg   eg  ee     ai  ai
#  egg      gg     ai            ia   ge    egeeaii   ag     aa  gi      gg    ag ig ig ei   iggiieegi  ga
#  aai      gg     gi           gi    ga    ai   ig   ae     ai  ag      ge    giii   egg    eg         ii
#  iegaggi   eagggae         aaag     ig    gaeei ig  aa     eg   igegiggig     ie     ag     eigeeeg   ga
#                                                                        ig
#                                                                gi     ig
#                                                                  egggeg
#
#
#                                                                                          Made by N
```

### **Python 2.7** version

 
 ```
#coding:utf-8

import time
#用字符画的方式<del>虚区</del>输出自己的名字，逐行打印并添加延迟。 Coding with Python 2.7
print(' gga')
time.sleep(0.5)
print(' ggg                           eg   ae                                                                eg')
time.sleep(0.5)
print(' eaa                           ga')
time.sleep(0.5)
print(' aaa      ig     ea            eg   ga    ggaaega   geieaggi     aagaiea   gii   eag   aea  gieggai   gg')
time.sleep(0.5)
print(' gia      ga     gg            ge   ig         ga   ei     ei   ig     gg   ee   agg   eg  ee     ai  ai')
time.sleep(0.5)
print(' egg      gg     ai            ia   ge    egeeaii   ag     aa  gi      gg    ag ig ig ei   iggiieegi  ga')
time.sleep(0.5)
print(' aai      gg     gi           gi    ga    ai   ig   ae     ai  ag      ge    giii   egg    eg         ii')
time.sleep(0.5)
print(' iegaggi   eagggae         aaag     ig    gaeei ig  aa     eg   igegiggig     ie     ag     eigeeeg   ga')
time.sleep(0.5)
print('                                                                       ig')
time.sleep(0.5)
print('                                                               gi     ig')
time.sleep(0.5)
print('                                                                 egggeg')
time.sleep(0.5)
print('')
time.sleep(0.5)
print('')
time.sleep(1)
print('                                                                                         Made by N')
#  gga
#  ggg                           eg   ae                                                                eg
#  eaa
#  aaa      ig     ea            eg   ga    ggaaega   geieaggi     aagaiea   gii   eag   aea  gieggai   gg
#  gia      ga     gg            ge   ig         ga   ei     ei   ig     gg   ee   agg   eg  ee     ai  ai
#  egg      gg     ai            ia   ge    egeeaii   ag     aa  gi      gg    ag ig ig ei   iggiieegi  ga
#  aai      gg     gi           gi    ga    ai   ig   ae     ai  ag      ge    giii   egg    eg         ii
#  iegaggi   eagggae         aaag     ig    gaeei ig  aa     eg   igegiggig     ie     ag     eigeeeg   ga
#                                                                        ig
#                                                                gi     ig
#                                                                  egggeg
#
#
#                                                                                          Made by N

 ```

## Something else: `Python 3` or `Python 2.7`?

For some reason, `print` function is replaced by `print()` in `Python 3` and newer version.  
However, in `Python 2.7`, both `print` and `print()` works with no difference. We can see this feature in [Wikipedia][1]:

> `Python 3.0`的变化主要在以下几个方面[13]：
>
> - `print`语句没有了，取而代之的是`print()`函数。可以使用`2to3`工具来自动转换。`Python 2.6`与`Python` 2.7部分地支持这种形式的print语法。在Python 2.6与Python 2.7里面，以下三种形式是等价的：
>```
>print "fish"
>print ("fish") #注意print后面有个空格
>print("fish") #print()不能带有任何其它参数
>```

Firstly, I chose the newer version simply because it's newer. But when I acknowledged that many science and calculating modules only worked on `Python 2`, I turned to the older version <del>with tears</del>.  
Now I find that modules are also updated to support the newest version.I know it's time to return to `Python 3`.

Oh, just take a rest, Python 2.

[1]:https://zh.wikipedia.org/zh-cn/Python#Python_3.0
