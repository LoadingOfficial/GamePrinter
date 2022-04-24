import os
import time
import json

import filesystem
from printer import image

config = {
    "directory": "path/to/directory",
    "refresh_time": 5
}

if os.path.isfile("config.json"):
    config = json.load(open("config.json"))
else:
    json.dump(config, open("config.json", "w"))
    exit()
        
# directory = "screenshots"

number = filesystem.number(config["directory"])
number_old = number
while True:
    number = filesystem.number(config["directory"])
    if int(number) > int(number_old):
        image(filesystem.latest(config["directory"]))
        number_old = number
    time.sleep(config["refresh_time"])