import colorama
from colorama import Fore
colorama.init(autoreset=True)
import requests
import http, re
http.client._is_legal_header_name = re.compile(b'[^\s][^:\r\n]*').fullmatch
import time, threading
import os
import random
import string
import emoji as ej
os.system("title Simple Raider ^| BlaQ#8358") 
import pyautogui, pyperclip
 
def joiner(invite, token):
    headers = {
                ":authority": "canary.discord.com",
                ":method": "POST",
                ":path": "/api/v9/invites/" + invite,
                ":scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": token,
                "content-length": "0",
                "cookie": "__dcfduid=75af9050ff6211ebad731ffdee3c037e; __sdcfduid=75af9051ff6211ebad731ffdee3c037e933998e6356b1dffdf296486c9c67f3f52108589d44d26d29febc86909e52537; __stripe_mid=b1d29ec9-19c8-41d7-9ace-e35266d8e9d1725cd3; __cfruid=402026f51d740991320e719ec5b87763fb9f0b58-1630164866",
                "origin": "https://canary.discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }
    src = requests.post("https://discordapp.com/api/v9/invites/" + invite, headers=headers)
    if src.status_code == 200:
        print(f" {Fore.CYAN}[+]{Fore.WHITE} Done")
 
def send_message(token, channel_id, text, antispam):
    request = requests.Session()
    headers = {'Authorization':token, 
     'Content-Type':'application/json', 
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    if antispam == "y":
        text += ' | ' + ''.join(random.choices((string.ascii_lowercase + string.digits), k=10))
    payload = {'content':text, 
     'tts':False}
    src = request.post(f"https://canary.discordapp.com/api/v6/channels/{channel_id}/messages", headers=headers, json=payload, timeout=10)
    if src.status_code == 200:
            print(f" {Fore.CYAN}[+]{Fore.WHITE} Message sent")
    return src

def spam(tokens, channel_id, text, antispam, delay):
    while True:
        token = random.choice(tokens)
        threading.Thread(target=send_message, args=(token, channel_id, text, antispam)).start()
        time.sleep(delay)
 
def randstr(lenn):
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text

def get_headers(token):
    return {'Content-Type':'application/json', 
     'Accept':'*/*', 
     'Accept-Encoding':'gzip, deflate, br', 
     'Accept-Language':'en-US', 
     'Cookie':f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US", 
     'DNT':'1', 
     'origin':'https://discord.com', 
     'TE':'Trailers', 
     'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9', 
     'authorization':token, 
     'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

def reaction(channel_id, message_id, emoji, token):
    try:
        headers = get_headers(token)
        emoji = ej.emojize(emoji, use_aliases=True)
        src = requests.put(f"https://discordapp.com/api/v6/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me", headers=headers)
        if src.status_code == 204:
           print(f" {Fore.CYAN}[+]{Fore.WHITE} Reaction  added")
    except:
        pass
 

banner = f"""  
 {Fore.CYAN}
    ██████  ██▓ ███▄ ▄███▓ ██▓███   ██▓    ▓█████     ██▀███   ▄▄▄       ██▓▓█████▄ ▓█████  ██▀███  
 ▒██    ▒ ▓██▒▓██▒▀█▀ ██▒▓██░  ██▒▓██▒    ▓█   ▀    ▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
 ░ ▓██▄   ▒██▒▓██    ▓██░▓██░ ██▓▒▒██░    ▒███      ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌▒███   ▓██ ░▄█ ▒
   ▒   ██▒░██░▒██    ▒██ ▒██▄█▓▒ ▒▒██░    ▒▓█  ▄    ▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄   
 ▒██████▒▒░██░▒██▒   ░██▒▒██▒ ░  ░░██████▒░▒████▒   ░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓ ░▒████▒░██▓ ▒██▒
 ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ░  ░▒▓▒░ ░  ░░ ▒░▓  ░░░ ▒░ ░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ░▒  ░ ░ ▒ ░░  ░      ░░▒ ░     ░ ░ ▒  ░ ░ ░  ░     ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
 ░  ░  ░   ▒ ░░      ░   ░░         ░ ░      ░        ░░   ░   ░   ▒    ▒ ░ ░ ░  ░    ░     ░░   ░ 
       ░   ░         ░                ░  ░   ░  ░      ░           ░  ░ ░     ░       ░  ░   ░     
                                                                   {Fore.LIGHTCYAN_EX}BlaQ#8358
                                

                                         {Fore.LIGHTCYAN_EX}[1] {Fore.WHITE}Joiner
                                         {Fore.LIGHTCYAN_EX}[2] {Fore.WHITE}Leaver
                                         {Fore.LIGHTCYAN_EX}[3] {Fore.WHITE}Channel Spammer
                                         {Fore.LIGHTCYAN_EX}[4] {Fore.WHITE}Token Checker
                                         {Fore.LIGHTCYAN_EX}[5] {Fore.WHITE}Typing Spammer
                                         {Fore.LIGHTCYAN_EX}[6] {Fore.WHITE}Reaction
 
"""

while True:
    os.system("cls")
    print("")
    print(banner)
    choice = input(f" {Fore.LIGHTCYAN_EX}> {Fore.WHITE}Choice: ")
    
    if choice == "1":
        tokens = open("tokens.txt", "r").read().splitlines()
        invite = input(f" Discord Invite: ")
        delay = float(input(f" Delay: "))
        invite = invite.replace("https://discord.gg/", "")
        invite = invite.replace("discord.gg/", "")
        invite = invite.replace("https://discord.com/invite/", "")        
 
        for token in tokens:
           time.sleep(delay)
           threading.Thread(target=joiner, args=(invite, token)).start()
 
    elif choice == "2":
        tokens = open("tokens.txt", "r").read().splitlines()
        server_id = input(f" Server ID: ")
        apilink = "https://discordapp.com/api/v9/users/@me/guilds/" + str(server_id)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token
                }
                requests.delete(apilink, headers=headers)
                print(f"{Fore.CYAN} [+]{Fore.WHITE} The token has successfully left the server")
  
    elif choice == "3":
        tokens = open("tokens.txt", "r").read().splitlines()
        channel_id = input(f" Channel ID: ")
        text = input(f" Message: ")
        delay = float(input(f" Delay: ")) 
        antispam = input(f" Append random string? (y/n): ")
 
        for token in tokens:
                threading.Thread(target=spam, args=(tokens, channel_id, text, antispam, delay)).start()
                 
    elif choice == "4":
       tokens = open("tokens.txt", "r").read().splitlines()
       validlist = []
       valid = 0
       invalid = 0
       locked = 0

       with open('tokens.txt') as (f):
            for line in f:
                token = line.strip('\n')
                headers = {'Content-Type':'application/json',  'authorization':token}
                url = 'https://discordapp.com/api/v6/users/@me/library'
                src = requests.get(url, headers=headers)

                if src.status_code == 200:
                    print(f" {Fore.LIGHTGREEN_EX}[+]{Fore.WHITE} Valid │ " + token)
                    validlist.append(token)
                    valid += 1
                elif src.status_code == 401:
                    print(f" {Fore.LIGHTRED_EX}[-]{Fore.WHITE} Invalid │ " + token)    
                    invalid += 1
                elif src.status_code == 403:
                    print(f" {Fore.RED}[-]{Fore.WHITE} Locked │ " + token)    
                    locked = +1 

                print("")
                print(f" {Fore.LIGHTGREEN_EX}Valid{Fore.WHITE}: {valid}")
                print(f" {Fore.LIGHTRED_EX}Invalid{Fore.WHITE}: {invalid}")
                print(f" {Fore.RED}Locked{Fore.WHITE}: {locked}")
                print("")
                print("")

                rem = input(f" Do you want remove Invalid and Locked tokens? (y/n): ")
                if rem == "y":
                    with open(f"tokens.txt", "w") as saveFile:
                        saveFile.write('\n'.join(validlist))
                        print(f" [{Fore.LIGHTGREEN_EX}+{Fore.WHITE}] Done")
                elif rem == "n":
                    pass

    elif choice == "5":
        text = input(f" Message: ")
        delay = float(input(f" Delay: "))
 
        print("") 
        print(f" You have 10 seconds to start typing")
        time.sleep(10)
        print("")
        while True:
            pyperclip.copy(text) 
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")
            print(f" {Fore.CYAN}[+]{Fore.WHITE} Message sent")
                   
    elif choice == "6":
        tokens = open("tokens.txt", "r").read().splitlines()
        channel_id = input(f" Channel ID: ")
        message_id = input(f" Message ID: ")
        emoji = input(f" Emoji: ")

        for token in tokens:
            threading.Thread(target=reaction, args=(channel_id, message_id, emoji, token)).start()
    os.system("cls")        