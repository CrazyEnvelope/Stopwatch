import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from PIL import Image, ImageTk

class Interface:
    def __init__(self,appTitle):
        self.setup(appTitle)

    def setup(self,appTitle):
        self.root = Tk()
        self.root.iconbitmap("images/chronometer.ico")
        self.root.title(appTitle)
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.root.configure(background="black")
        self.frames()
        self.label()
        self.images()
        self.buttons()
        self.startWatchButton()

    def frames(self):
        self.frame = Frame(self.root, bg = "#171B24")
        self.middleFrame = Frame(self.frame, bg="#171B24", width=300, height=70)
        self.bottomFrame = Frame(self.frame, bg="#171B24", width=400, height=70)


        self.frame.pack(fill="both", expand=True)
        self.middleFrame.place(in_= self.frame, relx=0.5, rely=0.5, anchor="center")
        self.bottomFrame.place(in_= self.frame, relx=0.5, rely=0.9, anchor="s")

    def label(self):
        self.labelForTimer = Label(self.middleFrame, text="00:00:00", fg="white", bg="#171B24",font="Arial 40")
        self.labelForTimer.place(in_=self.middleFrame, relx=0.5, rely=0.5, anchor="center")

    def images(self):
        playButtonImg = Image.open("images/play-button.png")
        pauseButtonImg = Image.open("images/pause-button.png")
        stopButtonImg = Image.open("images/stop.png")
        lapButtonImg = Image.open("images/red-flag.png")

        fixed_size = (64,64)

        playButtonImg_resized = playButtonImg.resize(fixed_size)
        pauseButtonImg_resized = pauseButtonImg.resize(fixed_size)
        stopButtonImg_resized = stopButtonImg.resize(fixed_size)
        lapButtonImg_resized = lapButtonImg.resize(fixed_size)

        self.playButtonImage = ImageTk.PhotoImage(playButtonImg_resized)
        self.pauseButtonImage = ImageTk.PhotoImage(pauseButtonImg_resized)
        self.stopButtonImage = ImageTk.PhotoImage(stopButtonImg_resized)
        self.lapButtonImage = ImageTk.PhotoImage(lapButtonImg_resized)

    def buttons(self):
        self.playButtonCentral = tkinter.Button(self.bottomFrame, image = self.playButtonImage, bg="#171B24", borderwidth=0)
        self.playButtonRight = tkinter.Button(self.bottomFrame, image = self.playButtonImage,bg="#171B24",borderwidth=0)
        self.pauseButtonRight = tkinter.Button(self.bottomFrame, image = self.pauseButtonImage,bg="#171B24",borderwidth=0)
        self.stopButtonLeft = tkinter.Button(self.bottomFrame, image = self.stopButtonImage,bg="#171B24",borderwidth=0)
        self.lapButtonLeft = tkinter.Button(self.bottomFrame, image = self.lapButtonImage,bg="#171B24",borderwidth=0)

    def startWatchButton(self):
        self.playButtonCentral.place(in_=self.bottomFrame, relx=0.5, rely=0.5, anchor="center")

    def pauseAndLapButton(self):
        self.pauseButtonRight.place(in_=self.bottomFrame, relx=0.8, rely=0.5, anchor="center")
        self.lapButtonLeft.place(in_=self.bottomFrame, relx=0.2, rely=0.5, anchor="center")

    def startAndStopButton(self):
        self.playButtonRight.place(in_=self.bottomFrame, relx=0.8, rely=0.5, anchor="center")
        self.stopButtonLeft.place(in_=self.bottomFrame, relx=0.2, rely=0.5, anchor="center")


    def lapListDisplay(self):

        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "Dark.Treeview",
            background="#252D3A",
            fieldbackground="#252D3A",
            foreground="white",
            borderwidth=0,
            relief="flat",
            rowheight=35,
        )

        style.configure(
            "Dark.Treeview.Heading",
            background="#171B24",
            foreground="white",
            font=("Helvetica", 10, "bold"),
            borderwidth=0,
            relief="flat",
            padding=(0, 10),
        )

        style.map(
            "Dark.Treeview.Heading",
            background=[("active", "#171B24"), ("pressed", "#171B24")],
            foreground=[("active", "white"), ("pressed", "white")],
            relief=[("active", "flat"), ("pressed", "flat")],
        )


        self.lapList = Treeview(self.frame, columns=["Number", "Interval", "ActualTime"],show="headings",height=7, style="Dark.Treeview")

        self.lapList.tag_configure("oddrow", background="#2B3442")
        self.lapList.tag_configure("evenrow", background="#252D3A")

        self.v_scrollbar = Scrollbar(self.frame, orient = VERTICAL, command = self.lapList.yview)
        self.lapList.configure(yscrollcommand = self.v_scrollbar.set)

        self.lapList.column("Number", width = 133, anchor = "center")
        self.lapList.heading("Number", text = "#", anchor = "center")
        self.lapList.column("Interval", width = 133, anchor = "center")
        self.lapList.heading("Interval", text = "LAP TIME", anchor = "center")
        self.lapList.column("ActualTime", width = 133, anchor = "center")
        self.lapList.heading("ActualTime", text = "TOTAL TIME", anchor = "center")

        self.lapList.place(in_=self.frame, relx=0.5, rely=0.45, anchor="center")


    def forgetCentralPlay(self):
        self.playButtonCentral.place_forget()

    def forgetPauseAndLapButton(self):
        self.pauseButtonRight.place_forget()
        self.lapButtonLeft.place_forget()

    def forgetStopAndPlayButton(self):
        self.playButtonRight.place_forget()
        self.stopButtonLeft.place_forget()

    def forgetLapFrame(self):
        self.lapList.place_forget()

    def labelTextMoveUp(self):
        self.middleFrame.place(in_=self.frame, relx=0.5, rely=0.1, anchor="center")

    def labelTextMoveDown(self):
        self.middleFrame.place(in_=self.frame, relx=0.5, rely=0.5, anchor="center")

    def main(self):
        self.root.mainloop()

