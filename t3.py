# -*- coding: utf-8 -*-

import xiaoqi1
import t1
import c1
import e1
import os


def xiangsidu():            
    list2 = t1.chinesexiaoqi(r"G:/WorkSpace/bishe/test/chinese/0001.txt")
    li = os.listdir(r"G:/test/english")
    a = []
    k = 0
    for p in li:
        pathname = os.path.join(r"G:/test/english", p)
        list1 = xiaoqi1.xiaoqi(pathname)
        list3 = [val for val in list1 if val in list2]
        print len(list3)*3.0/(len(list1)+len(list2))
        a.append(len(list3)*3.0/(len(list1)+len(list2)))
    return a


def xiangsidu1():            
    list2 = c1.chinesexiaoqi(r"G:/WorkSpace/bishe/test/chinese/0001.txt")
    li = os.listdir(r"G:/test/english")
    a = []
    for p in li:
        pathname = os.path.join(r"G:/test/english",p)
        list1 = e1.xiaoqi(pathname)
        s = c1.distance(list2,list1)
        a.append(s)
    return a
