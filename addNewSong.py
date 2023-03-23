import json

flag = True
with open('songCollection.json') as json_file_org:
    condensed = json.load(json_file_org)
    possibleNew = input("insert new song via in the following form: name,artist,date (without spaces)\n")
    possibleArr = possibleNew.split(",")
    if possibleArr[0] in condensed:
        if condensed[possibleArr[0]][0] == possibleArr[1]:
            print("Error: Song already in")
            flag = False
    if flag:
        condensed[possibleArr[0]] = (possibleArr[1],possibleArr[2])

        json_object = json.dumps(condensed, indent=4)
        with open('songCollection.json','w') as json_file_write:
            json_file_write.write(json_object)
            print("Success")