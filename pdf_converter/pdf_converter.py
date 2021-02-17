#we are going made pdf_converter
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as msg
from fpdf import FPDF
import os
class Pdf_con(Tk):
    def __init__(self,title,bg,_size):
        super().__init__()
        self.title(title)
        self.geometry(_size)
        self.config(bg=bg)
        self._data=StringVar()
        self.l1=Label(self,text="Text to pdf converter",fg="white",font="serif 12 bold",bg="#0984e3",width=36,height=3)
        self.l1.pack(side=TOP,fill=BOTH)
        self.but_q=Button(self,text="Quit",borderwidth=5,bg="#d35400",fg="white",font="serif 12 bold",cursor="spider",command=self.quit)
        self.but_q.pack(side=BOTTOM,fill="both")
        self._l2=Label(self,text="choose File or Path",bg="pink",font="serif 10 bold")
        self._l2.place(x=0,y=112,height=60)
        self._ent=Entry(self,font="serif 13 bold",fg="red",textvariable=self._data)
        self._ent.place(x=200,y=112,height=60,width=370)
        self._butt=Button(self,text="Convert",bg="#2d3436",fg="white",cursor="pirate",font="serif 12 bold",relief=GROOVE,borderwidth=5,command=self._convert)
        self._butt.place(x=210,y=200,width=190)
        self._butt2=Button(self,text="Open",bg="#0984e3",fg="black",cursor="plus",font="serif 12 bold",relief=GROOVE,borderwidth=4,command=self._func)
        self._butt2.place(x=10,y=200,width=120)
    
    def _func(self):
        self.filename=fd.askopenfilename()
        self._data.set(str(self.filename))

    def _convert(self):
        try:
            self._a=self._data.get()
            self.pdf=FPDF()
            self.pdf.add_page()
            self.pdf.set_font("Times",size=10)
            self.fd=open(self._a,"r")

            for i in self.fd:
                self.pdf.cell(100,10,txt=i,ln=90)

            self.pdf.output("pdf.pdf")

            msg.showinfo("sucess","sucessfully converted to pdf...")
        except:
            msg.showerror("error","something error find out!")



       

if __name__=='__main__':
    _window=Pdf_con("pdf converter","#3742fa","590x670")
    _window.mainloop()
