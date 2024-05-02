# messingwith_JSON.py
# this programis to demonstrate how to work with JSON files in Python3
# author: atacan

import json

electricBill = {
    'name' : 'Andrew',
    'amount' : '99999'
}

with open("storeData.json", "wt") as f:
    json.dump(electricBill, f) # writes the dictionary object to the file as a JSON object
    # 'dump' is to write and 'load' is to read

FILENAME="storeData.json"
with open(FILENAME, "rt") as file:
    for line in file:
        print (line, end='')

# I am assuming that json has already been imported

# assuming theat the file storedata exists and contains json
with open("storeData.json", "rt") as f:
    readDict = json.load(f) # reads the file and converts the JSON object into a list of dictionary 
    print (readDict["amount"])