import time

class Stopwatch:

    def __init__(self, appinterface):
        self.count = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.secondString = 0
        self.minuteString = 0
        self.hourString = 0

        self.timer = False
        self.appInterface = appinterface
        self._next_tick_time = None

    def startWatch(self):

        if self.timer is not True:
            self.timer = True
            self._next_tick_time = time.perf_counter()
            self.resumeWatch()

        self.appInterface.forgetCentralPlay()
        self.appInterface.pauseAndLapButton()
        self.appInterface.forgetStopAndPlayButton()

    def stopWatch(self):
        self.timer = False

        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.secondString = self.seconds
        self.minuteString = self.minutes
        self.hourString = self.hours

        self.updateText()

        self.appInterface.forgetStopAndPlayButton()
        self.appInterface.startWatchButton()

    def pauseWatch(self):
        self.timer = False
        self.appInterface.forgetPauseAndLapButton()
        self.appInterface.startAndStopButton()

    def lapWatch(self):
        pass

    def resumeWatch(self):
        if self.timer is True:
            self.count += 1

            if self.count == 100:
                self.seconds += 1
                self.count = 0

            if self.seconds == 60:
                self.minutes += 1
                self.seconds = 0

            if self.minutes == 60:
                self.hours += 1
                self.minutes = 0
                self.seconds = 0

            self.updateText()

            self._next_tick_time += 0.01
            delay_ms = max(0, int((self._next_tick_time - time.perf_counter()) * 1000))
            self.appInterface.root.after(delay_ms, self.resumeWatch)

    def updateText(self):
        self.secondString = self.seconds
        self.minuteString = self.minutes
        self.hourString = self.hours

        if (self.seconds < 10):
            self.secondString = f"0{self.seconds}"

        if (self.minutes < 10):
            self.minuteString = f"0{self.minutes}"

        if (self.hours < 10):
            self.hourString = f"0{self.hours}"

        self.appInterface.labelForTimer.configure(text=f"{self.hourString}:{self.minuteString}:{self.secondString}")