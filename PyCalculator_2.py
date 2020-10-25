#!/usr/bin/python3
# -*- coding UTF-8 -*-
"""
##########################################################

Name:       Py Calculator 1.0
Created by: Christian Moran
e-mail:     christianrmoran86@gmail.com
More code:  http://github.com/chrisrm86

##########################################################
"""
from tkinter import *
from tkinter.messagebox import *
from sys import exit

class PyCalculator_1():
    def __init__(self, master=None, **configs):
        self.app = master
        self.app.geometry("238x270")
        #self.app.geometry("238x312")
        self.app.resizable(False,False)
        self.app.title("PyCalculator")
        #self.app.iconbitmap('calc.ico')

        self.stringContents = ''
        self.displayStr = StringVar(self.stringContents)
        self.displayStr.set('0')

        self.modContests =''
        self.displayMod = StringVar(self.modContests)

        menubar = Menu(self.app)
        menubar.add_command(label="Dark Mode", command=self.dark_mode)
        menubar.add_command(label="About", command=self.info)
        menubar.add_command(label="Exit", command=exit)
        self.app.config(menu=menubar)

        self.principal_container = Frame(self.app, borderwidth=4, bg="white")
        self.principal_container.pack(expand=YES, fill=BOTH)

        self.screen_section = Frame(self.principal_container, bg="#2F4F4F", height=50, width=50, borderwidth=2)
        self.screen_section.pack(side=TOP, expand=NO, fill=BOTH, padx=2, pady=2)

        self.area1 = Frame(self.principal_container, bg="#2F4F4F", height=10, width=100, borderwidth=2)
        self.area1.pack(side=TOP, expand=NO, fill=BOTH, padx=2, pady=2)

        self.area2 = Frame(self.area1, bg="white", height=15, width=20, borderwidth=2)
        self.area2.pack(side=RIGHT, expand=YES, fill=BOTH, padx=2, pady=2)

        #self.area3 = Frame(self.principal_container, bg="#2F4F4F", height=28, width=25, borderwidth=2)
        #self.area3.pack(side=TOP, expand=YES, fill=BOTH, padx=2, pady=2)

        #label1=Label(self.area3, text="", bg="#2F4F4F", fg="white")
        #label1.pack()

        self.buttons_section =Frame(self.principal_container, bg="#2F4F4F", height=4, width=4, borderwidth=2, )
        self.buttons_section.pack(side=BOTTOM, expand=NO, fill=BOTH, padx=2, pady=2)

        self.visor = Label(self.screen_section, anchor=E, justify=CENTER, relief=SUNKEN, bg="black", fg="white", height=2, width=30, padx=3, pady=3, textvariable=self.displayStr)
        self.visor.grid(column=0, row=0, columnspan=4)
        self.visor2 = Label(self.area2, textvariable=self.displayMod, anchor=E, justify=RIGHT, bg="white").pack(side=RIGHT, expand=YES)

        title_label=Label(self.area1, text="[   Basic Calculator    ]", bg="#2F4F4F", fg="white")
        title_label.pack(side=LEFT, expand=NO, fill=None)
        b0 = Button(self.buttons_section, text="0", width= 7, height=2, bg="#D4D4D2", fg="black", command=lambda:self.printNum('0')).grid(column=0, row=6)
        b1 = Button(self.buttons_section, text="1", width=7, height=2, bg="#D4D4D2", fg="black", command=lambda: self.printNum('1')).grid(column=0,row=5)
        b2 = Button(self.buttons_section, text="2", width=7, height=2, bg="#D4D4D2", fg="black", command=lambda: self.printNum('2')).grid(column=1,row=5)
        b3 = Button(self.buttons_section, text="3", width=7, height=2, bg="#D4D4D2", fg="black", command=lambda: self.printNum('3')).grid(column=2,row=5)
        b4 = Button(self.buttons_section, text="4", width=7, height=2, bg="#D4D4D2", fg="black", command=lambda: self.printNum('4')).grid(column=0, row=4)
        b5 = Button(self.buttons_section, text="5", width=7, height=2, bg="#D4D4D2", fg="black", command=lambda: self.printNum('5')).grid(column=1, row=4)
        b6 = Button(self.buttons_section, text="6", width=7, height=2, bg="#D4D4D2", fg="black", command=lambda: self.printNum('6')).grid(column=2, row=4)
        b7=Button(self.buttons_section, text="7", width=7, height=2, bg="#D4D4D2", fg="black", command=lambda: self.printNum('7')).grid(column=0, row=3)
        b8=Button(self.buttons_section, text="8", width=7, height=2, bg="#D4D4D2", fg="black", command=lambda: self.printNum('8')).grid(column=1, row=3)
        b9=Button(self.buttons_section, text="9", width=7, height=2, bg="#D4D4D2", fg="black", command=lambda:self.printNum('9')).grid(column=2, row=3)

        addition= Button(self.buttons_section, text="+", width=5, height=2, bg="#FF9500", fg="white", command=lambda:self.modify('+')).grid(column=3, row=6)
        subtraction = Button(self.buttons_section, text="-", width=5, height=2, bg="#FF9500", fg="white", command=lambda:self.modify('-')).grid(column=3, row=5)
        multiplication = Button(self.buttons_section, text="x", width=5, height=2,bg="#FF9500", fg="white", command=lambda:self.modify('x')).grid(column=3, row=4)
        division = Button(self.buttons_section, text="/", width=5, height=2, bg="#FF9500", fg="white", command=lambda:self.modify('/')).grid(column=3, row=3)

        delete=Button(self.buttons_section, text="C", width=7, height=2, bg="#D4D4D2", fg="black", command=lambda:self.clear()).grid(column=1, row=6)
        equal=Button(self.buttons_section, text="=", width=7, height=2, bg="#D4D4D2", fg="black", command=lambda:self.modify('=')).grid(column=2, row=6)

        self.expression = {'left':None, 'modifier':None,'right':None}

    def printNum(self, num):
        if self.stringContents.find('0') == 0:
            self.stringContents = ''
        if num == '.' and '.' in self.stringContents: return
        self.stringContents += num
        self.displayStr.set(self.stringContents)

    def modify(self, modifier):
        if self.stringContents == '' and self.expression['left'] != None:
            pass
        elif self.stringContents == '' and self.expression['left'] == None:
            self.expression['left'] = 0
            self.printNum('0')
            self.stringContents = ''
        elif self.expression['modifier'] == None or \
            (self.stringContents != '' and self.expression['left'] == None):
            self.expression['left'] = self.stringContents
            self.stringContents = ''
        elif self.stringContents != '' and self.expression['left'] != None:
            self.evaluate(self.expression, modifier)
        self.modContents = modifier
        self.expression['modifier'] = modifier
        self.displayMod.set(self.modContents)

    def evaluate(self, expression, modifier = None):
        if self.expression['left'] == None or self.stringContents == '':
            pass
        else:
            self.expression['right'] = self.stringContents
            self.stringContents = ''
            equals = 0
            if expression['modifier'] == 'x':
                equals = float(expression['left']) * float(expression['right'])
            elif expression['modifier'] == '/':
                equals = float(expression['left']) / float(expression['right'])
            elif expression['modifier'] == '+':
                equals = float(expression['left']) + float(expression['right'])
            else:
                equals = float(expression['left']) - float(expression['right'])
            if equals == int(equals):
                equals = int(equals)
                self.expression['left'] = equals
                self.expression['right'] = None
                if modifier != None:
                    self.expression['modifier'] = modifier
                    self.modContents = modifier
                else:
                    self.expression['modifier'] = None
                    self.modContents = ''
                self.displayMod.set(self.modContents)
                self.displayStr.set(str(equals))
                self.stringContents = ''

    def clear(self):
        self.expression['left'] = None
        self.expression['right'] = None
        self.expression['modifier'] = None
        self.modContents = ''
        self.stringContents = ''
        self.displayStr.set(self.stringContents)
        self.displayMod.set(self.modContents)
        self.displayStr.set('0')

    def zero(self):
        self.displayStr.set('0')

    def dark_mode(self):
        self.principal_container.config(bg="#2e4053")
        #self.buttons_section.config(bg="#2e4053")
        label1.config(bg="orange")

    def light_mode(self):
        pass

    def info(self):
        showinfo(title="About", message="Developed by Christian Morán.\rE-mail: christianrmoran86@gmail.com.\rMore code:www.github.com/chrisrm86")

if __name__=='__main__':
    root=Tk()
    PyCalculator_1(root)
    root.mainloop()