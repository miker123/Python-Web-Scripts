#!/usr/bin/env python
#Author: Mike R
#Date: 4/29/2016
#Purpose: To be able to download any extension the user desires and analyze the results

from Tkinter import *
import Tkinter
import tkMessageBox, os

def donothing():
	filewin = Toplevel(root)
	button = Button(filewin, text="Do nothing button")
	button.pack()
   
def helloCallBack():
    #validating URL
    dataTP="python googTest.py " + E1.get()
    os.system(dataTP)
    #check to see if invalid Add-On

root = Tk()
root.wm_title("Panic At The WebStore!")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

L1 = Label(root, text="Chrome GUID")
L1.pack( side = LEFT)
E1 = Entry(root, bd =5)

B = Tkinter.Button(root, text ="Submit", command = helloCallBack)

B.pack(side = RIGHT)

E1.pack(side = RIGHT)
root.mainloop()
