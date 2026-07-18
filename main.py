from bidings import Bidings
from interface import Interface
from stopwatch import Stopwatch

if __name__ == '__main__':
    appInterface = Interface("Stopwatch")
    stopWatch = Stopwatch(appInterface)
    bidings = Bidings(appInterface, stopWatch)

    appInterface.main()
