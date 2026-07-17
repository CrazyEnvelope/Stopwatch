from bidings import Bidings
from interface import Interface
from stopwatch import Stopwatch

if __name__ == '__main__':
    app = Interface("Stopwatch")
    stopWatch = Stopwatch()
    bidings = Bidings(app, stopWatch)

    app.main()
