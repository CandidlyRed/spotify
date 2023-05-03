import json

# Opening JSON file
with open('/home/memorybox/Desktop/spotify/songCollection.json') as json_file_org:
    condensed = json.load(json_file_org)
    with open('/home/memorybox/Desktop/spotify/endsong.json') as json_file:
        rawdata = json.load(json_file)
        for entry in rawdata:
            if (not entry["skipped"]) and (entry["ms_played"] > 6000) and (entry["master_metadata_track_name"] not in condensed):
                condensed[entry["master_metadata_track_name"]] = (entry["master_metadata_album_artist_name"],entry["ts"])

    json_object = json.dumps(condensed, indent=4)
    with open('/home/memorybox/Desktop/spotify/songCollection.json','w') as json_file_write:
        json_file_write.write(json_object)