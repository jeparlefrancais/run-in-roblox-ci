curl http://setup.roblox.com/RobloxStudioLauncherBeta.exe --output rbxinstall.exe
rbxinstall.exe -API api.json
py bin/wait-for-file.py api.json