import json

def pins():
    with open('data/pins.json') as file:
        return json.load(file)
