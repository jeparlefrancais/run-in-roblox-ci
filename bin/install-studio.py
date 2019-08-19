import os
import sys
import subprocess

local_app_data = os.getenv('LOCALAPPDATA')

print('LOCALAPPDATA =', local_app_data)

roblox = os.path.join(local_app_data, 'Roblox')

print('Install Roblox...')
install_process = subprocess.Popen(['rbxinstall.exe'])

timeout_count = 0

while timeout_count < 30:
    try:
        install_process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        timeout_count += 1
        print('Retry?', not os.path.exists(roblox))

print('Studio install expired.')

if os.path.exists(roblox):
    print('Roblox content:')
    print(os.listdir(roblox))
else:
    print('Roblox does not exists :(')
