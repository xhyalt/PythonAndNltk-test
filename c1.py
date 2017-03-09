# -*- coding: utf-8 -*-


import jieba.posseg as pseg
import jieba.analyse
import re
import string
from nltk.corpus import wordnet as wn


queue = []
queue.append(wn.synset('entity.n.01'))
dict = {queue[0]: [1]}
dict[queue[0]].append(len(queue[0].hyponyms()))
dict[queue[0]].append(bin(1)[2:])
levelbit = [1,2,4,6,9,7,8,9,9,9,9,7,7,5,5,6,5,4,4,1]



while len(queue) > 0:
    count = 1;
    node = queue.pop(0)
    for child in node.hyponyms():

        queue.append(child)
        level = dict[node][0]+1
        codeLen = levelbit[level-1]
        codestr = dict[node][2]+bin(count)[2:].zfill(codeLen)
        dict[child] = [level,len(child.hyponyms()),codestr]
        
        count = count + 1
 
for x in dict:
    dict[x][2] = string.ljust(dict[x][2],117,'0')
        
    
def findsynset(list):
    listsynset = []
    for lemma in list:
            for i in wn.synsets(lemma, lang = 'cmn'):
                listsynset.append(i)
    listhash = []
    for i in listsynset:
        if dict.has_key(i):
            listhash.append(dict[i][2])
    return listhash


def distance(list1,list2):
    max1 = 0
    max2 = 116
    m = 116
    for p in list1:
        while m >= 0:
            if p[m]=='0':m = m-1
            else:break
        for q in list2:
            r = q[0]
            i = 0
            j = 0
            k = 0
            while k < 117:
                if p[k]==r[k]:k=k+1
                else:
                    if i == 0:
                        i = k
                        k = k + 1
                    else:
                        j = k
                        k = k + 1
            if i > max1:
                max1 = i
                max2 = m
    return max1*1.0/max2
  


def chinesetag(pathname):
    result =  open(pathname).read()
    tags = jieba.analyse.extract_tags(result,topK=30)
  #  print tags
  #  print u'\u8bed\u4e49', u'\u7b97\u6cd5', u'\u6d88\u6b67', u'\u76f8\u5173\u6027', u'\u590d\u6742\u5ea6', u'WordNet', u'\u5bc6\u5ea6', u'\u4e00\u7ec4', u'\u4e4b\u95f4', u'LSH', u'SemCor', u'\u54c8\u5e0c', u'\u8fdb\u884c', u'\u4ece\u800c', u'\u63d0\u51fa', u'\u5927\u5927\u964d\u4f4e', u'\u540d\u8bcd', u'\u4e00\u79cd', u'\u5316\u4e3a', u'\u91cf\u5316'
    return tags


def chinesexiaoqi(pathname):
    
    k = 0
    l = 11
    listnon = chinesetag(pathname)
    senseen = []
    while k < len(listnon):
        W = listnon[k]
        C = findsynset(W)     
        if len(C) <> 0:
            senseen = C
            break
        k = k+1
    return senseen
    
    
    
                
                
            
            
