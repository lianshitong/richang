#!/usr/bin/env python
#coding:utf-8
#要求:给定一个不超过5位的正整数，判断其有几位。

number = int(input("请输入一个不超过5位的正整数:"))

# 分段思维
if number >= 1000:
    if number >= 10000:
        print(5)
    else:
        print(4)
else:
    if number >= 100:
        print(3)
    elif number >= 10:
        print(2)
    else:
        print(1)



# 一般常规思维
# if number >=0 and number <= 9:
#     print(1)
# elif number >=10 and number <=99:
#     print(2)
# elif number >=100 and number <= 999:
#     print(3)
#elif number >= 1000 and number <= 9999:
#      print(4)
#elif number >=10000 and number <= 99999:
#      print(5)
# else:
#     print("out of range")
