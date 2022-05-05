import threading
import time
import random

import printer
import gui
import log
import configuration
import directory

running = False

configuration.load()

if configuration.first == True:
    gui.clear("status")
    print(log.timestamp() + "Welcome!")
else:
    gui.clear("status")
    print(log.timestamp() + "Welcome back!")

gui.update_value("path", configuration.GamePrinter["path"])
gui.update_value("refresh_interval", configuration.GamePrinter["refresh_interval"])

configuration.load()

def GamePrinter(random):
    configuration.load() # why won't it load the configuration?
    
    number_of_files_old = directory.number_of_files(configuration.GamePrinter["path"])

    while True:
        global running
        if running == False:
            break

        number_of_files = directory.number_of_files(configuration.GamePrinter["path"])

        while number_of_files > number_of_files_old:
            difference = number_of_files - number_of_files_old

            if difference == 1:
                print(log.timestamp() + "Found 1 new file")

            else:
                print("Found " + str(difference) + " new files")
                print("")

            while number_of_files > number_of_files_old:
                print("Printing" + directory.latest_files(configuration.GamePrinter["path"], difference)[difference - 1] + " ...")
                printer.image(directory.latest_files(configuration.GamePrinter["path"], difference)[difference - 1])
                number_of_files_old += 1
                difference = number_of_files - number_of_files_old
        
        if number_of_files == number_of_files_old:
            gui.clear("status")
            print(log.timestamp() + "No new files")
            
        time.sleep(configuration.GamePrinter["refresh_interval"])

thread_id = random.random()
thread = threading.Thread(target = GamePrinter, args = (thread_id, ))

while True:
    event, values = gui.window.read()

    if event == "start_stop":
        if running == False:
            gui.clear("status")
            print(log.timestamp() + "Starting thread...")
            
            running = True
            thread_id = random.random()
            thread = threading.Thread(target = GamePrinter, args = (thread_id, ))
            thread.start()
            
            gui.update_icon("start_stop", gui.icon("stop"))

        else:
            gui.clear("status")
            print(log.timestamp() + "Stopping thread...")

            running = False
            try:
                thread.join()

            except:
                pass

            gui.update_icon("start_stop", gui.icon("start"))

    elif event == "save":
        if values["path"] != "" and values["refresh_interval"] != "":

            if running == True:
                gui.clear("status")
                print(log.timestamp() + "Stopping thread...")

                running = False
                try:
                    thread.join()

                except:
                    pass

                gui.update_icon("start_stop", gui.icon("start"))
            
            configuration.save(values["path"], values["refresh_interval"])

            gui.clear("status")
            print(log.timestamp() + "Saved!")

        else:
            gui.clear("status")
            print(log.timestamp() + "Error: \"Folder path\" and/or \"Refresh Interval\" is empty.")
        
    elif event == gui.WIN_CLOSED or event == "exit":
        if running == True:
            running = False
            thread.join()
            gui.window.close()

        break