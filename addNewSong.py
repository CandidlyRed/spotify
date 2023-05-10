import json

flag = True
with open('/home/memorybox/Desktop/spotify/songCollection.json') as json_file_org:
    condensed = json.load(json_file_org)
    possibleNew = input("insert new song via in the following form: name,artist,date (without spaces)\n")
    possibleArr = possibleNew.encode('utf-8').decode('unicode-escape').split(",")
    if possibleArr[0] in condensed:
        if condensed[possibleArr[0]][0] == possibleArr[1]:
            print("Error: Song already in")
            flag = False
    if flag:
        condensed[possibleArr[0]] = (possibleArr[1],possibleArr[2])

        json_object = json.dumps(condensed, indent=4)
        with open('/home/memorybox/Desktop/spotify/songCollection.json','w', encoding='utf-8') as json_file_write:
            json_file_write.write(json_object)
            print("Success")
