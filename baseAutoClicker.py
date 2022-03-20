import tkinter as tk
import pyautogui
import time
import threading


def blink():
    def run():
        while (switch == True):
            print('next Auto...BLINK...')
            '''
            if (isinstance(attDelayEntry.get(), float)):
                    time.sleep(attDelayEntry.get())
            else:
            '''
            time.sleep(delay)
            pyautogui.click()
            if switch == False:
                break
    thread = threading.Thread(target=run)
    thread.start()

def switchon():
    global switch
    global delay
    delay = 0.8
    #delay = float(attDelayEntry)
    delay = float(attDelayEntry.get())
    switch = True
    print('switch on')
    onbutton["state"] = "disabled"    
    blink()

def switchoff():
    print('switch off')

    global switch
    onbutton["state"] = "normal"
    switch = False

def kill():
    root.destroy()
    exit()

root = tk.Tk()          
root.geometry("400x400")

attDelayEntry = tk.Entry()
attDelayEntry.pack()
onbutton = tk.Button(root, text = "auto ATTACK ON", command= switchon)
onbutton.pack()    
offbutton =  tk.Button(root, text = "auto ATTACK OFF", command = switchoff)
offbutton.pack() 
killbutton = tk.Button(root, text = "EXIT", command = kill)
killbutton.pack()


