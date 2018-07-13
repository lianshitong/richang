#!/usr/bin/env python

import psutil
import os


# 获取python进程pid
def getPID():
    pid = psutil.Process(os.getpid())
    return pid

def getCPUstate(interval=1):
    pass

# 获取物理内存使用率
def getMemorystate():
    phymem = (psutil.virtual_memory()).percent
    percent = "内存使用率:{}%".format(phymem)
    return percent

def getDiskInfo():
    all_partitions = psutil.disk_partitions(all)
    print(all_partitions[0])
    print(all_partitions[1])
    print(type(all_partitions[0]))

class getNetInfo:
    def getEthInfo(key):
        net_if_addr = psutil.net_if_addrs()
        print(net_if_addr['以太网'])
        print(type(net_if_addr['以太网']))

a = getNetInfo()
a.getEthInfo()