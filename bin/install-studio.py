import os
import sys
import subprocess

file_name = 'api.json'

print('Install Roblox...')
install_process = subprocess.Popen(['rbxinstall.exe', '-API', file_name])

timeout_count = 0

while timeout_count < 30:
    try:
        install_process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        timeout_count += 1
        print('is file written?', os.path.exists(file_name))

print('Too much tries')

local_app_data = os.getenv('LOCALAPPDATA')

print('LOCALAPPDATA =', local_app_data)

roblox = os.path.join(local_app_data, 'Roblox')

if os.path.exists(roblox):
    print('Roblox content:')
    print(os.listdir(roblox))
else:
    print('Roblox does not exists :(')
