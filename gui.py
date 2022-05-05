import time
from PySimpleGUI import *

LOOK_AND_FEEL_TABLE["GamePrinter_light"] = {"BACKGROUND": "#FFFFFF",
                                        "TEXT": "#000000",
                                        "INPUT": "#EEEEEE",
                                        "TEXT_INPUT": "#000000",
                                        "SCROLL": "#EEEEEE",
                                        "BUTTON": ("#000000", "#EEEEEE"),
                                        "PROGRESS": ("#000000", "#1DE9B6"),
                                        "BORDER": 0, "SLIDER_DEPTH": 0, "PROGRESS_DEPTH": 0}

theme("GamePrinter_light")

def icon(name):
    location = "resources/icons/" + name + ".png"
    return location

banner = [[Image(icon("GamePrinter")), Text("GamePrinter", font = ("Segoe UI Semibold", 24))]]

controls = [[Button("", image_filename = icon("start"), key = "start_stop")]]

status = [[Text("Status", font = ("Segoe UI",16))],
         [Multiline(key="status", size=(48, 2), font = ("Consolas"), disabled = True, enter_submits= False, autoscroll = True, auto_refresh = True, do_not_clear = True, reroute_stdout = True)]]

configure = [[Text("Settings", font = ("Segoe UI",16))],
             [Text("Folder path"), Input(key = "path", change_submits = True), FolderBrowse(key = "path_browse")],
             [Text("Refresh interval"), Spin(key = "refresh_interval", values=[x+1 for x in range(100)], initial_value = 5), Text("seconds")],
             [Button("Save", key = "save")]]

main_window = [[banner],
           [Column(controls), VerticalSeparator(color = "#EEEEEE"), Column(status)],
           [HorizontalSeparator(color = "#EEEEEE")],
           [Column(configure)]]

window = Window(layout = main_window, title = "", font = ("Segoe UI", 10), margins = (8, 12), finalize = True, debugger_enabled = False)

def update_icon(key, icon):
    if icon != "":
        window.find_element(key).Update(image_filename = icon)

def update_value(key, value):
    window.find_element(key).Update(value)

def clear(key):
    window.find_element(key).Update(value = "")