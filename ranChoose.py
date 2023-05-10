import json
import random
  
def randomChoose():
    with open('/home/memorybox/Desktop/spotify/songCollection.json', encoding='utf-8') as json_file_org:
        condensed = json.load(json_file_org)
        name,val = random.choice(list(condensed.items()))
        return (name,val[0],val[1])
