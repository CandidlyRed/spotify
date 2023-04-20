# TODO: Implement time blockers

import time
import random
import sys
from ranChoose import randomChoose
# from mpd import MPDClient
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5 import QtGui

# figure out what terminal command to set up

start = time.time()

PERIOD_OF_TIME = 50400 # 3600=1hr, this is currently set as 14 hours

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("MemoryBox")
        # setting  the geometry of window
        self.setGeometry(0, 70, 500, 240)

        self.timeLeft = QLabel("00:00")
        self.setCentralWidget(self.timeLeft)

        self.authorTitle = QLabel("Woo - Someone")
        self.setCentralWidget(self.authorTitle)

while True :
    # time.sleep(600.0 - ((time.time() - start) % 600.0))
    # rand = random.randint(1,110)
    # if rand == 1:
    if True:
        name,artist,date = randomChoose()
        while (name == 'null'):
            name,artist,date = randomChoose()

        # client = MPDClient()
        # client.timeout = 120
        # client.idletimeout = 120
        # client.connect("localhost", 6600)
        # print(client.mpd_version)
        # client.clear()
        # client.add("yt:https://youtu.be/7PR3I23cd4I")
        # client.play()
        # client.close()
        # client.disconnect()

        # time.sleep(0.3)

        
        App = QApplication(sys.argv)
        
        window = Window()
        window.show()
        App.exec()


        print("success")
        break

    if time.time() > start + PERIOD_OF_TIME : break
