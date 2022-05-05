import os
import json

import log

location = "resources/configuration/GamePrinter.json"

GamePrinter_default = {"path": "", "refresh_interval": 5}

def load():
    with open(location) as file:
        global GamePrinter
        GamePrinter = json.load(file)

def save(path, refresh_interval):
    GamePrinter = {"path": path, "refresh_interval": refresh_interval}
    json.dump(GamePrinter, open(location, "w"))
    load()

if os.path.isfile(location):
    load()
    first = False

else:
    json.dump(GamePrinter_default, open(location, "w"))
    load()
    first = True