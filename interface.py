import tkinter
from idlelib import autoexpand
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview


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
        self.label()
        self.buttons()
        self.startWatchButton()

    def frames(self):
        self.frame = Frame(self.root, bg = "black")
        self.middleFrame = Frame(self.frame, bg="white", width=300, height=70)
        self.bottomFrame = Frame(self.frame, bg="blue", width=400, height=70)


        self.frame.pack(fill="both", expand=True)
        self.middleFrame.place(in_= self.frame, relx=0.5, rely=0.5, anchor="center")
        self.bottomFrame.place(in_= self.frame, relx=0.5, rely=0.9, anchor="s")

    def label(self):
        self.labelForTimer = Label(self.middleFrame, text="00:00:00", fg="black", font="Arial 40")
        self.labelForTimer.place(in_=self.middleFrame, relx=0.5, rely=0.5, anchor="center")

    def buttons(self):
        self.playButtonCentral = tkinter.Button(self.bottomFrame, text = "Start", background="white")
        self.playButtonRight = tkinter.Button(self.bottomFrame, text = "Start", background="white")
        self.pauseButtonRight = tkinter.Button(self.bottomFrame, text="Pause", background="white")
        self.stopButtonLeft = tkinter.Button(self.bottomFrame, text="Stop", background="white")
        self.lapButtonLeft = tkinter.Button(self.bottomFrame, text="Lap", background="white")

    def startWatchButton(self):
        self.playButtonCentral.place(in_=self.bottomFrame, relx=0.5, rely=0.5, anchor="center")

    def pauseAndLapButton(self):
        self.pauseButtonRight.place(in_=self.bottomFrame, relx=0.8, rely=0.5, anchor="center")
        self.lapButtonLeft.place(in_=self.bottomFrame, relx=0.2, rely=0.5, anchor="center")

    def startAndStopButton(self):
        self.playButtonRight.place(in_=self.bottomFrame, relx=0.8, rely=0.5, anchor="center")
        self.stopButtonLeft.place(in_=self.bottomFrame, relx=0.2, rely=0.5, anchor="center")


    def lapListDisplay(self):
        self.lapFrame = Frame(self.frame, bg="white", width=400, height=300)
        self.lapFrame.place(in_=self.frame, relx=0.5, rely=0.2, anchor="n")

        self.lapList = Treeview(self.lapFrame, columns=["Number", "Interval", "ActualTime"],show="headings",height=15)

        self.v_scrollbar = Scrollbar(self.lapFrame, orient = VERTICAL, command = self.lapList.yview)
        self.lapList.configure(yscrollcommand = self.v_scrollbar.set)

        self.lapList.column("Number", width = 133, anchor = "center")
        self.lapList.column("Interval", width = 133, anchor = "center")
        self.lapList.column("ActualTime", width = 133, anchor = "center")

        self.lapList.place(in_=self.lapFrame, relx=0.0, rely=-0.08, anchor="nw")
        self.v_scrollbar.place(in_=self.lapFrame, relx=0.95, rely=0, anchor="nw",height=300)


    def forgetCentralPlay(self):
        self.playButtonCentral.place_forget()

    def forgetPauseAndLapButton(self):
        self.pauseButtonRight.place_forget()
        self.lapButtonLeft.place_forget()

    def forgetStopAndPlayButton(self):
        self.playButtonRight.place_forget()
        self.stopButtonLeft.place_forget()

    def forgetLapFrame(self):
        self.lapFrame.place_forget()

    def labelTextMoveUp(self):
        self.middleFrame.place(in_=self.frame, relx=0.5, rely=0.1, anchor="center")

    def labelTextMoveDown(self):
        self.middleFrame.place(in_=self.frame, relx=0.5, rely=0.5, anchor="center")

    def main(self):
        self.root.mainloop()

