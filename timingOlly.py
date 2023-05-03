# TODO: Implement time blockers

import time
import random
import sys
import requests
import re, requests, subprocess, urllib.parse, urllib.request
import json
import urllib
from datetime import datetime
from ranChoose import randomChoose
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
        self.countDown = False
        self.start = 0
        self.counter = 0
        # set the title
        self.setWindowTitle("MemoryBox for Seraphina")
        # setting  the geometry of window
        self.setGeometry(0, 65, 480, 265)
        
        self.space = QLabel("")
        self.timeLeft = QLabel("00:00")
        self.timeLeft.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignBottom)
        self.authorTitle = QLabel("Memory - Box")
        self.authorTitle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.image = QLabel(self)
        self.image.setGeometry(190, 35, 100, 100)
        self.image.setStyleSheet("background-image : url(/home/memorybox/Desktop/spotify/whitescreen.jpg);border: 1px solid white;")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.space)
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
    
    # action method
    def clickme(self):
        if (not self.isNotPlaying) and (not self.started):
            self.countDown = False
            self.activePlayer()
            # printing pressed
            # print("pressed")

    def recurring_timer(self):
        now = datetime.now()
        current_time = int((now.strftime("%H:%M:%S"))[0:2])
        if (current_time >= 9) and (current_time <= 22): # active from hour 9 am to 10 pm
            # rand = random.randint(1,50400) # about 6 times a week? (based on number of seconds)
            rand = random.randint(1,10)
            if (rand == 1) and (self.isNotPlaying):
                subprocess.Popen("./ytplayvlc " + "https://www.youtube.com/watch?v=dgD-Lakn8SA" + " 18",shell=True)
                self.isNotPlaying = False
                self.countDown = True
                self.start = time.time()
                self.authorTitle.setText("loading...")
            elif (self.countDown) and (not self.started) and ((time.time() - self.start) > 150):
                subprocess.Popen("killall vlc",shell=True)
                self.isNotPlaying = True
                self.countDown = False
                self.started = False
                self.counter = 0
                self.timeLeft.setText("00:00")
                self.authorTitle.setText("Memory - Box")
                self.image.setStyleSheet("background-image : url(/home/memorybox/Desktop/spotify/whitescreen.jpg);border: 1px solid white;")
            elif (not self.countDown) and (self.started) and ((time.time() - self.start) > 1000):
                subprocess.Popen("killall vlc",shell=True)
                self.isNotPlaying = True
                self.countDown = False
                self.started = False
                self.counter = 0
                self.timeLeft.setText("00:00")
                self.authorTitle.setText("Memory - Box")
                self.image.setStyleSheet("background-image : url(/home/memorybox/Desktop/spotify/whitescreen.jpg);border: 1px solid white;")
            elif self.started:
                self.counter += 1
                minutes = str(self.counter // 60)
                seconds = str(self.counter % 60)
                analogTime = (minutes if (len(minutes) == 2) else ("0" + minutes)) + ":" + (seconds if (len(seconds) == 2) else ("0" + seconds))
                self.timeLeft.setText(analogTime)

    def activePlayer(self):
        self.started = True
        self.start = time.time()
        subprocess.Popen("killall vlc",shell=True)
        name,artist,date = randomChoose()
        while (name == 'null'):
            name,artist,date = randomChoose()
        
        self.authorTitle.setText(artist + ": " + name + " - (" + date[:-10] + ")")
        music_name = artist + " " + name
        query_string = urllib.parse.urlencode({"search_query": music_name})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])   

        img_url = "{}".format(search_results[0])
        img_data = requests.get("https://img.youtube.com/vi/" + img_url + "/hqdefault.jpg").content
        with open('/home/memorybox/Desktop/spotify/image_name.jpg', 'wb') as handler:
            handler.write(img_data)
        img = Image.open('/home/memorybox/Desktop/spotify/image_name.jpg')
        width,height = img.size
        img = img.crop((width * .25, height * .15, width * .75, height * .85))
        img = img.resize((100, 100))
        img.save('/home/memorybox/Desktop/spotify/image_name.jpg')
        self.image.setStyleSheet("background-image : url(image_name.jpg);border: 1px solid white;")

        subprocess.Popen("./ytplayvlc " + clip2 + " 18",shell=True)


App = QApplication(sys.argv)
window = Window()
App.exec()
