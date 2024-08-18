# PyBrowser 1.0, by PyBrowser Incorporated.
import os
import time
import webbrowser

def start():
    os.system('clear')
    print("PyBrowser Version 1.0")
    print("Property of PyBrowser Incorporated. Forks of this utility are allowed under acknowledgement.")
    print("-----------------------------------------------------------------------------------------------")
    print("Start Menu")
    print("1. Use PyBrowser 1.0")
    print("2. Exit the utility")
    print("Select an option:")
    select = input(" ")

    if select == "1":
        os.system('clear')
        print("Starting PyBrowser...")
        time.sleep(3)
        os.system('clear')
        pybrowser()

    elif select == "2":
        os.system('clear')
        print("Exiting PyBrowser...")
        time.sleep(4)
        os.system('clear')
        print("You can now exit the utility safely!")

    else:
        print("Option not valid. Try again.")
        time.sleep(5)
        os.system('clear')
        start()


def pybrowser():
    print("PyBrowser Version 1.0")
    print("Property of PyBrowser Incorporated. Forks of this utility are allowed under acknowledgement.")
    print("-----------------------------------------------------------------------------------------------")
    search = input("Enter the URL: ")
    time.sleep(3)
    os.system('clear')
    print("Loading...")
    time.sleep(3)
    webbrowser.open(search)
    os.system('clear')
    start()


start()
