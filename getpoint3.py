# coding: utf-8
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import matplotlib.pyplot as plt
import numpy as np

def taxcalculation():
    filename=answer1.get()
    # filename = r"C:\Users\duanh\Desktop\025an_anal_tors.dat"
    ttxt = np.loadtxt(filename)
    xx = ttxt[:, 0]
    yy = ttxt[:, 1]
    # print(ttxt[:,0])

    plt.figure()
    plt.scatter(xx, yy,color='green')
    print('choose some point')
    num = answer2.get()
    lii = []
    pointchoose=[]
    i=0
    # undo=chvarUn.get()


    while i < num:

            # i = i - 1
        t = plt.ginput(1)
        tx = t[0][0]
        ty = t[0][1]
        d = np.array((xx - tx) ** 2 + (yy - ty) ** 2)
        minindex = d.argmin()
        if list(ttxt[minindex][:]) in lii:
            plt.scatter(ttxt[minindex][0], ttxt[minindex][1], color='green')
            lii.remove(list(ttxt[minindex][:]))
            i=i-1
        else:
            plt.scatter(ttxt[minindex][0],ttxt[minindex][1],color='red')
            # print(ttxt[minindex][:])
            lii.append(list(ttxt[minindex][:]))
            i=i+1

    flename = '取点.txt'
    fle = open(flename, mode='w')
    for i in lii:
        for j in i:
            fle.write(str(j)+' ')
        fle.write('\n')

    fle.close()

    plt.show()

root = tk.Tk()
root.title("取点器")
window_left = ttk.Frame(root)
window_left.pack(ipadx=10, ipady=10, fill='y', side=tk.LEFT)
label = ttk.Label(window_left, text="输入文件路径")
label.pack(padx=10, pady=10)
answer1=tk.StringVar()
entry1 = ttk.Entry(window_left, width=20, textvariable=answer1)
entry1.pack()
label2 = ttk.Label(window_left, text="多少个点？")
label2.pack(padx=10, pady=10)
answer2 = tk.IntVar()
entry2 = ttk.Entry(window_left, width=20, textvariable=answer2)
entry2.pack()
btn = ttk.Button(window_left, width=20,text="取点", command=taxcalculation)
btn.pack(padx=10, pady=10)

root.mainloop()


