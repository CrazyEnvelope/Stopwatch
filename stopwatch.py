
class Stopwatch:

    def __init__(self):
        self.count = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.timer = False

    def startWatch(self):
        print("start")
        if self.timer is not True:
            self.timer = True
            self.resumeWatch()

    def stopWatch(self):
        self.timer = False

    def pauseWatch(self):
        self.timer = False

    def lapWatch(self):
        pass

    def resumeWatch(self):
        if self.timer is True:
            self.count += 1

            if self.count == 100:
                self.seconds += 1
                self.count = 0

            if self.seconds == 60:
                self.minute += 1
                self.seconds = 0

            if self.minutes == 60:
                self.hours += 1
                self.minutes = 0
                self.seconds = 0