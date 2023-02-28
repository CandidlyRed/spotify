# TODO: implement database based off of spotify zip file
## relevant fields: timestamp, track_name, uri?
## x: skipped, repeated, ms_played > 60 seconds
import json

# TODO: Load current data, save. open endsong.json, add to current data, rerwrite to songCollection.json


condensed = {}
# Opening JSON file
with open('endsong.json') as json_file:
    rawdata = json.load(json_file)