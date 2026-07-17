import tkinter
from tkinter import *

class Interface:
    def __init__(self,appTitle):
        self.setup(appTitle)

    def setup(self,appTitle):
        self.root = Tk()
        self.root.title(appTitle)
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.root.configure(background="black")
        self.frames()
        self.buttons()

    def frames(self):
        self.frame = Frame(self.root, bg = "black")
        self.middleFrame = Frame(self.frame, bg="white", width=300, height=70)
        self.bottomFrame = Frame(self.frame, bg="blue", width=400, height=70)

        self.frame.pack(fill="both", expand=True)
        self.middleFrame.place(in_= self.frame, relx=0.5, rely=0.5, anchor="center")
        self.bottomFrame.place(in_= self.frame, relx=0.5, rely=0.9, anchor="s")

    def buttons(self):
        self.playButtonCentral = tkinter.Button(self.bottomFrame, text = "Start", background="white")
        self.playButtonRight = tkinter.Button(self.bottomFrame, text = "Start", background="white")
        self.pauseButtonRight = tkinter.Button(self.bottomFrame, text="Pause", background="white")
        self.stopButtonLeft = tkinter.Button(self.bottomFrame, text="Stop", background="white")
        self.lapButtonLeft = tkinter.Button(self.bottomFrame, text="Lap", background="white")

        self.playButtonCentral.place(in_= self.bottomFrame, relx=0.5, rely=0.5, anchor="center")
        self.playButtonRight.place(in_=self.bottomFrame, relx=0.8, rely=0.5, anchor="center")
        self.pauseButtonRight.place(in_=self.bottomFrame, relx=0.8, rely=0.5, anchor="center")
        self.stopButtonLeft.place(in_=self.bottomFrame, relx=0.2, rely=0.5, anchor="center")
        self.lapButtonLeft.place(in_=self.bottomFrame, relx=0.2, rely=0.5, anchor="center")



    def main(self):
        self.root.mainloop()