# TODO: Implement time blockers
# TODO: Implement random generators

import time
import random
from ranChoose import randomChoose
from mopidy_json_client import MopidyClient

# figure out what terminal command to set up

start = time.time()

PERIOD_OF_TIME = 50400 # 3600=1hr, this is currently set as 14 hours

while True :
    # time.sleep(600.0 - ((time.time() - start) % 600.0))
    # rand = random.randint(1,110)
    # if rand == 1:
    if True:
        name,artist,time = randomChoose()
        while (name == 'null'):
            name,artist,time = randomChoose()
        
        mopidy = MopidyClient(
            ws_url='ws://localhost:6680/mopidy/ws',
            error_handler=on_server_error,)
        
        mopidy.tracklist.clear()
        # mopidy.tracklist.add(['yt:https://youtu.be/7PR3I23cd4I'])
        # mopidy.playback.play()

        # while(mopidy.playback.get_state(timeout=5) != 'stopped'):
        #     time.sleep(5)
        # mopidy.disconnect()
        print("success")
        break

    if time.time() > start + PERIOD_OF_TIME : break

def on_server_error(error):
        print('[SERVER_ERROR] ', error, format='error')