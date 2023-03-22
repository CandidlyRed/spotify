import json

# Opening JSON file
with open('songCollection.json') as json_file_org:
    condensed = json.load(json_file_org)
    with open('endsong.json') as json_file:
        rawdata = json.load(json_file)
        for entry in rawdata:
            if (not entry["skipped"]) and (entry["ms_played"] > 6000) and (entry["master_metadata_track_name"] not in condensed):
                condensed[entry["master_metadata_track_name"]] = (entry["master_metadata_album_artist_name"],entry["ts"])

    json_object = json.dumps(condensed, indent=4)
    with open('songCollection.json','w') as json_file_write:
        json_file_write.write(json_object)

def addNewSong(name,artist,date):
    with open('songCollection.json') as json_file_org:
        condensed = json.load(json_file_org)
        if name in condensed:
            return -1
        else:
            condensed[name] = (artist,date)
            json_object = json.dumps(condensed, indent=4)
            with open('songCollection.json','w') as json_file_write:
                json_file_write.write(json_object)
            return 1