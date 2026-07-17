
class Bidings:

    def __init__(self, app, stopWatch):
        self.app = app
        self.stopWatch = stopWatch
        self.bidingButtons()

    def bidingButtons(self):
        self.app.playButtonCentral.configure(command=self.stopWatch.startWatch)
        self.app.playButtonRight.configure(command=self.stopWatch.startWatch)
        self.app.pauseButtonRight.configure(command=self.stopWatch.pauseWatch)
        self.app.stopButtonLeft.configure(command=self.stopWatch.stopWatch)
        self.app.lapButtonLeft.configure(command=self.stopWatch.lapWatch)
