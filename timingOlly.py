# TODO: Implement time blockers
# TODO: Implement random generators

import time
import random
from ranChoose import randomChoose
from mopidy_json_client import MopidyClient
from mopidy_json_client.formatting import print_nice

# figure out what terminal command to set up

start = time.time()

PERIOD_OF_TIME = 50400 # 3600=1hr, this is currently set as 14 hours

class MemoryBox():
    def __init__(self):
        
        self.state = 'stopped'
        self.uri = None

        self.mopidy = MopidyClient(
            ws_url='ws://localhost:6680/mopidy/ws',
            error_handler=self.on_server_error,
            connection_handler=self.on_connection,
            autoconnect=False,
            retry_max=10,
            retry_secs=10
        )

        self.bind_events()
        self.mopidy.connect()

    def on_server_error(self, error):
        print_nice('[SERVER_ERROR] ', error, format='error')
    
    def on_connection(self,conn_state):
        if conn_state:
            # Initialize mopidy track and state
            self.state = self.mopidy.playback.get_state(timeout=5)
            tl_track = self.mopidy.playback.get_current_tl_track(timeout=15)
            track_playback_started(tl_track)
        else:
            self.state = 'stopped'
            self.uri = None

    def track_playback_started(self, tl_track):
        track = tl_track.get('track') if tl_track else None
        self.uri = track.get('uri') if track else None
        print_nice('> Current Track: ', track, format='track')

    def bind_events(self):
        self.mopidy.bind_event('playback_state_changed', self.playback_state_changed)

    def playback_state_changed(self, old_state, new_state):
        self.state = new_state
        print_nice('> Playback state changed to ', self.state)

    def execute_command(self, command, args=[]):
        if (command == 'exit'):
            self.mopidy.disconnect()
            time.sleep(0.2)
            exit()
        elif (command == 'play'):
            if args:
                if unicode(args[0]).isnumeric():
                    self.mopidy.playback.play(tlid=int(args[0]))
            else:
                self.mopidy.playback.play()
        elif (command == 'clear'):
            self.mopidy.tracklist.clear()
        elif (command == 'add'):
            self.mopidy.tracklist.add(uris=['podcast+http://feeds.feedburner.com/aokishouse#http://traffic.libsyn.com/steveaoki/037_AOKIS_HOUSE_-_STEVE_AOKI.mp3'])

while True :
    # time.sleep(600.0 - ((time.time() - start) % 600.0))
    # rand = random.randint(1,110)
    # if rand == 1:
    if True:
        name,artist,date = randomChoose()
        while (name == 'null'):
            name,artist,date = randomChoose()

        activate = MemoryBox()
        time.sleep(10)
        activate.execute_command("add")
        time.sleep(0.3)
        activate.execute_command("play")


        print("success")
        break

    if time.time() > start + PERIOD_OF_TIME : break
