# -*- coding: utf-8 -*-


import nltk
from nltk.corpus import wordnet as wn
import jieba.analyse
import re
import string

queue = []
queue.append(wn.synset('entity.n.01'))   #连接到根上位词
dict = {queue[0]: [1]}
dict[queue[0]].append(len(queue[0].hyponyms()))   #下位词
dict[queue[0]].append(bin(1)[2:])
levelbit = [1,2,4,6,9,7,8,9,9,9,9,7,7,5,5,6,5,4,4,1]



while len(queue) > 0:
    count = 1;
    node = queue.pop(0)    #第一个元素
    for child in node.hyponyms():

        queue.append(child)
        level = dict[node][0]+1
        codeLen = levelbit[level-1]
        codestr = dict[node][2]+bin(count)[2:].zfill(codeLen)  #返回指定长度的字符串
        dict[child] = [level,len(child.hyponyms()),codestr]
        
        count = count + 1
 
for x in dict:
    dict[x][2] = string.ljust(dict[x][2],117,'0')


def lowsamebit(list):
    list.sort()
    jieguo = bin(int(list[0],2) ^ int(list[-1],2))[2:]
    strb = str(jieguo)
    return len(strb)

def density(list):
    len1 = len(list)
    if (lowsamebit(list) - 53) > 0:
        max = lowsamebit(list) - 70
    else:
        max = 0
    return (len1 ** 2)/(1.2 ** max)


    
def findsynset(list):
    listsynset = []
    for lemma in list:
        listtemp = wn.synsets(lemma, pos = wn.NOUN)
        if len(listtemp):
            listsynset.extend(listtemp)
    listhash = []
    if listsynset:
        for i in listsynset:
            if dict.has_key(i):
                listhash.append(dict[i][2])
    return listhash


def biaoji(pathname):
    sentence =  open(pathname).read()
    tags = jieba.analyse.extract_tags(sentence,topK=20)
 #   print tags
    return tags

def xiaoqi(pathname):
    
    k = 0
    l = 5
    listnon = biaoji(pathname)
    senseen = []
    while k < len(listnon):
        MaxDensity = 0
        R = []
        W = listnon[k:(k+2*l+1)]
        C = findsynset(W)
        C.sort()
        p = len(C)
        for i in range(0, p):
            for j in range(i + 1, p + 1):
                C1 = C[i:j+1]
                C2 = findsynset(listnon[k+l : k+l+1])
                C3 = [val for val in C1 if val in C2]
                countjiao = len(C3)
                if (1 <= countjiao <=2 ):
                    Density = density(C1)
                    if Density > MaxDensity:
                        MaxDensity = Density
                        R = C3
        if len(R):
            senseen.append(R[0:1])
        k = k+1
    return senseen



