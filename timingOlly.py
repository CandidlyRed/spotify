# TODO: Implement time blockers

import time
import random
import sys
import requests
from ranChoose import randomChoose
# from mpd import MPDClient
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PIL import Image

# figure out what terminal command to set up

PERIOD_OF_TIME = 50400 # 3600=1hr, this is currently set as 14 hours

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.isNotPlaying = True
        self.started = False
        self.start = 0
        # set the title
        self.setWindowTitle("MemoryBox for Seraphina")
        # setting  the geometry of window
        self.setGeometry(0, 65, 480, 265)
        
        self.img_url = "Iz7xuqdkeMg" # Default grey
        self.img_data = requests.get("https://img.youtube.com/vi/" + self.img_url + "/hqdefault.jpg").content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(self.img_data)
        img = Image.open('image_name.jpg')
        width,height = img.size
        img = img.crop((width * .15, 0, width * .85, height))
        img = img.resize((100, 100))
        img.save('image_name.jpg')

        self.timeLeft = QLabel("\n\n00:00")
        self.timeLeft.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignBottom)
        self.authorTitle = QLabel("Memory - Box")
        self.authorTitle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.image = self.UiComponents()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.timeLeft)
        self.layout.addWidget(self.authorTitle)

        # self.layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)
        
        self.button = QPushButton(self)
        self.button.setGeometry(190, 35, 100, 100)
        self.button.clicked.connect(self.clickme)
        self.button.setStyleSheet("border: 1px solid white;")
        
        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def UiComponents(self):
    
        # creating a push button
        image = QLabel(self)

        # setting geometry of button
        image.setGeometry(190, 35, 100, 100)

        # adding action to a button
        # button.clicked.connect(self.clickme)

        # setting image to the button
        image.setStyleSheet("background-image : url(image_name.jpg);border: 1px solid white;")
    
    # action method
    def clickme(self):
        if not self.isNotPlaying:
            self.started = True
            self.activePlayer()
            # printing pressed
            print("pressed")

    def recurring_timer(self):
        rand = random.randint(1,396000)
        # if (rand == 1) and (self.isNotPlaying):
        if self.isNotPlaying:
            print("hii")
            self.isNotPlaying = False
            self.start = time.time()
            self.authorTitle.setText("loading...")
        else:
            if ((time.time() - self.start) > 60) and (not self.started):
                self.isNotPlaying = True
                self.authorTitle.setText("Memory - Box")

    def activePlayer(self):
        self.started = False
        name,artist,date = randomChoose()
        while (name == 'null'):
            name,artist,date = randomChoose()
        
        self.authorTitle.setText(artist + ": " + name + " - (" + date[:-10] + ")")


# while True :
#     # time.sleep(600.0 - ( % 600.0))

#     if True:


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
App.exec()
