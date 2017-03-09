# -*- coding: utf-8 -*-



import nltk
from nltk.corpus import wordnet as wn
import re
import string

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
        listtemp = wn.synsets(lemma, pos = wn.NOUN)
        if len(listtemp):
            listsynset.extend(listtemp)
    listhash = []
    if listsynset:
        for i in listsynset:
            if dict.has_key(i):
                listhash.append(dict[i][2])
    return listhash


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

def biaoji(pathname):
    list1 = []
    sentence =  open(pathname).read()
    sentence = sentence.decode('ascii', 'ignore')

    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    for i in tagged:
       if re.match(r'NN*', i[1]):
           if wn.morphy(i[0].lower()):
               list1.append(wn.morphy(i[0].lower()))
 #   print list1
    return list1

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
#    print senseen
    return senseen
