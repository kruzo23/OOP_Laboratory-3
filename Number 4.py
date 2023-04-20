from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl = Label(win,text="<-- Click to Change the color of the button", borderwidth=1,relief='raised')
        self.lbl.place(x=130,y=150)
        self.btn = Button(win, text="Color",bg='Blue',fg='Red',command = self.Change)
        self.btn.place(x=80,y=150)
    def Change(self):
        self.btn.config(bg='Yellow')


window = Tk()
mywin = MyWindow(window)
window.geometry("500x200+10+10")
window.title("Button")
window.mainloop()

