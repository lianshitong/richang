#!/usr/bin/env python
# coding:utf-8
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2018/7/11'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    return inc
print(counter(1))

foo = counter(10)
foo1 = counter(10)
print(id(foo))
print(foo())
print(foo1())

# sorted


lst = [1,2,5,4,3,6,7]
def sort(iterable,key=lambda a,b:a<b,reverse=False):
    ret = []
    for x in iterable:
        for i,y in enumerate(ret):
            flag = key(x,y) if reverse else key(y,x)
            if flag:
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret

print(sort(lst))