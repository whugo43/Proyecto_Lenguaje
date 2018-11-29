from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry
from Lex_Python import recibirtokens
from Yacc_Python import validate
from plagio import plagio
import os
class App(Frame):
    def comparar(self):
        expr = entry1.get ("1.0", 'end')
        expr2 = entry2.get ("1.0", 'end')
        if len(expr) == 1 or len(expr2) == 1 :
            self.errorMsg('error')
        else:
            return res.set(plagio(expr,expr2))
    def lexico(self):

        expr =entry1.get ("1.0", 'end')
        if len(expr) == 1:
            self.errorMsg('error')
        else:
            tokens = recibirtokens (expr)
            return res.set (tokens)

    def lexico2(self):
        expr2 = entry2.get ("1.0", 'end')
        if len(expr2) == 1:
            self.errorMsg('error')
        else:
            tokens = recibirtokens (expr2)
            return res.set (tokens)

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Comparador de dos programas")
        self.parent.geometry('850x500')
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global entry1
        global entry2
        global expr
        expr = StringVar()
        global res
        res = StringVar()

        global expr2
        expr2 = StringVar()
        global res2
        res2 = StringVar()

        ######PRIMER CODIGO

        frame0 = Frame(self)#
        frame0.pack(fill=X)

        frame1 = Frame(self)#
        frame1.pack(fill=X)

        lbl1 = Label(frame0, text="Programa 1:")
        lbl1.pack(side=LEFT, padx=150, pady=5)

        entry1 = Text(frame1,width=45, height=10)
        entry1.pack(side=LEFT, anchor=N,padx=30, pady=20, ipadx=0, ipady=20)

        frame3 = Frame(self)#
        frame3.pack(fill=X)

        btnlex = Button(frame3 , text="Lexico",command=self.lexico)
        btnlex.pack(side=LEFT, anchor=N, padx=100, pady=5)

        btnsint = Button(frame3, text="Sintáctico", command=self.validate)
        btnsint.pack(side=LEFT, anchor=NW, padx=0, pady=5)
        ######SEGUNDO CODIGO


        lbl2 = Label (frame0, text="Programa 2:")
        lbl2.pack (side=LEFT, anchor=N, padx=205, pady=5)

        entry2 = Text (frame1, width=45, height=10)
        entry2.pack ( anchor=N,padx=10,pady=20, ipadx=0, ipady=20)

        btnomparar = Button (frame3, text="Comparar", command=self.comparar)
        btnomparar.pack (side=LEFT, anchor=N, padx=85, pady=5)


        btnlex2 = Button (frame3, text="Lexico",command=self.lexico2)
        btnlex2.pack (side=LEFT, anchor=NW, padx=0, pady=5)

        btnsint2 = Button (frame3, text="Sintáctico", command=self.validate2)
        btnsint2.pack (side=LEFT, anchor=N, padx=100, pady=5)

        frame5 = Frame(self)#
        frame5.pack(fill=X)


        frame4 = Frame(self)#
        frame4.pack(fill=X)
        lbl3 = Label(frame4, text="Resultados :")
        lbl3.pack(side=LEFT, padx=5, pady=5)

        result = Label(frame4,textvariable=res)
        result.pack(padx=5,pady=5, expand=True)




    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Enter your expression')

    def validate(self):
        expr =entry1.get ("1.0", 'end')
        if len(expr) == 1:
            self.errorMsg('error')
        else:
            result = validate(expr)
            last_line = 'Correct!'
            file = open ('res.txt', 'r')
            for linea in file.readlines ():
                if linea == 'Syntax error!\n':
                    last_line = 'Syntax error!'
            file.close ()
            os.remove ('res.txt')

            res.set(last_line)

    def validate2(self):
        expr2 =entry2.get ("1.0", 'end')
        if len(expr2) == 1:
            self.errorMsg('error')
        else:
            result = validate(expr2)
            last_line = 'Correct!'
            file = open ('res.txt', 'r')
            for linea in file.readlines ():
                if linea == 'Syntax error!\n':
                    last_line = 'Syntax error!'
            file.close ()
            os.remove ('res.txt')

            res.set(last_line)



def main():
    root = Tk()
    root.geometry("300x140")
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()

