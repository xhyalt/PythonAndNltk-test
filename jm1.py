# -*- coding: utf-8 -*-

from Tkinter import *
import t3



def xin():
    global root
    a = t3.xiangsidu()
    k = 0
    while (k<len(a)):
        b = a[k]
        s = Label(root,text = b)
        s.pack()
        k = k + 1
    
def xin1():
    global root
    a = t3.xiangsidu1()
    k = 0
    while (k<len(a)):
        b = a[k]
        s = Label(root,text = b)
        s.pack()
        k = k + 1



root = Tk()
root.wm_title("中英文联合指纹剽窃检测系统")
#root.iconbitmap("C:\Users\a\Desktop\11.ico")
w1 = Label(root,text ="欢迎进入中英文联合指纹剽窃检测系统！")
w1.pack()
w2 = Button(None,text = "快速过滤",command = xin1)
w2.pack()
w3 = Button(None,text ="详细检测",command = xin)
w3.pack()
root.mainloop()
