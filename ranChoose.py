# TODO: lookup on mopidy and run
import json
import random
  
def randomChoose():
    with open('songCollection.json') as json_file_org:
        condensed = json.load(json_file_org)
        name,date = random.choice(list(condensed.items()))
        return (name,date)