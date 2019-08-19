import sys
import winreg


REGISTRY_KEY = r'Software\\Roblox\\RobloxStudioBrowser'
DOMAIN_KEY = r'roblox.com'
COOKIE_KEY = r'.ROBLOSECURITY'


with winreg.OpenKey(winreg.HKEY_CURRENT_USER, REGISTRY_KEY) as main_handle:

    with winreg.OpenKey(
        main_handle,
        DOMAIN_KEY,
        access=winreg.KEY_WRITE,
    ) as roblox_dot_com:

        winreg.SetValueEx(roblox_dot_com, COOKIE_KEY, 0, winreg.REG_SZ, os.environ[sys.argv[1]])
