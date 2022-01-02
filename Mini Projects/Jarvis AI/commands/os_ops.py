import os
import subprocess as sp

paths = {
    'notepad': 'C:\\Windows\\notepad.exe',
    'chrome': 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
    'discord': 'C:\\Users\\hatim\\AppData\\Local\\Discord\\app-0.0.306\\Discord.exe',
    'calculator': 'C:\\Windows\\System32\\calc.exe'
}

def open_camera():
    sp.run('start microsoft.windows.camera:',shell=True)

def open_notepad():
    os.startfile(paths['notepad'])

def open_discord():
    os.startfile(paths['discord'])

def open_chrome():
    os.startfile(paths['chrome'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])


