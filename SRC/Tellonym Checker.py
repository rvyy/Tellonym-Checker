import requests,colorama,json,threading,ctypes
from ctypes import windll
from colorama import Fore

colorama.init()


count = 0
print(Fore.LIGHTMAGENTA_EX+'''
  _______   _ _                                _____ _               _             
 |__   __| | | |                              / ____| |             | |            
    | | ___| | | ___  _ __  _   _ _ __ ___   | |    | |__   ___  ___| | _____ _ __ 
    | |/ _ \ | |/ _ \| '_ \| | | | '_ ` _ \  | |    | '_ \ / _ \/ __| |/ / _ \ '__|
    | |  __/ | | (_) | | | | |_| | | | | | | | |____| | | |  __/ (__|   <  __/ |   
    |_|\___|_|_|\___/|_| |_|\__, |_| |_| |_|  \_____|_| |_|\___|\___|_|\_\___|_|   
                             __/ |                                                 
                            |___/           Made by @rv.y                                                                       ''')

print(Fore.LIGHTRED_EX)

try:
    file = open('list.txt')
    print("[+] Successfully loaded list.txt")
except FileNotFoundError:
    input("[-] Press Enter To Create list.txt")
    open('list.txt','w').write('')
try:
    filef = open('settings.txt')
    print("[+] Successfully loaded settings.txt")
except FileNotFoundError:
    input("[-] Press Enter To Create settings.txt")
    open('settings.txt','w').write('''
{"settings" : {
	"Name": "@rv.y",
	"Webhook": "https://discord.com/api/webhooks/1014520152617926756/ac-SV6q6Iakr166xkALvND4VDbfpvSqWJMv0ysZRGnoyZuPsaVgWsmfNjxNrxwxUbNR6",
	"url/img": "https://giffiles.alphacoders.com/170/170955.gif",
        "token": "5536706031:AAHcDyjSJQTv7K2Y-LNBcc3uX6gghygBpEk",
        "ID": "2016608757"
}}

                                   ''')

print('[+] Send [1] Telegram , [2] Discord ? : ',end='')
e = int(input())

ee = open("settings.txt","r").read()

json_settings = json.loads(ee)
Name = json_settings["settings"]["Name"]
Webhook = json_settings["settings"]["Webhook"]
urlimg = json_settings["settings"]["url/img"]
token = json_settings["settings"]["token"]
ID = json_settings["settings"]["ID"]

print('[+] Threads ? : ',end='')
thread = int(input())

def r():
    global count
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '__cfduid=d9a45d5a0d1610e2a1abf30dac99aa7681613198934; _ga=GA1.2.1551905763.1613198948; _gid=GA1.2.767379040.1613198948; __cf_bm=ee7ac75044152eb1d2ad2f130402990e23eb0cda-1613232593-1800-AQ08xpweTVOHARq3LOG08YITD6T71cgZNqq41jhl8gtsnAg3eEVY5jwwMSOZloDO+EAv3V2SX2xaOSJKBnM5cBEPYNza54sWGauQeMsRKPnrnKMf2jKcta+uoo5ZWQV9ag==; _gat=1; __rtgt_sid=kl3x176qgjlsv2',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        }
    while True:
        user = file.readline().split('\n')[0]
        url = f'https://tellonym.me/{user}'
        req = requests.get(url, headers=headers)
        if (user == ""):
            file.close()
            exit()
        if req.status_code == 404:
            count += 1
            open('Available Users.txt', 'a').write(f'{user}\n')
            print(Fore.GREEN + f"{count} | {user} - Available")
            if e == 1:
                try:
                    tele = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=- Tellonym Checker -\n\nAvailable : {user}\n\nProgrammed by @rv.y"
                    tel = requests.post(tele)
                except:pass
            if e == 2:
                try:
                    urlsf = Webhook
                    datatg = {
                        "username" : ""
                        }
                    datatg["embeds"] = [
                        {
                            "description" : f'**Available : @{user}**',
                            "thumbnail" : {"url": urlimg},
                            "footer" : {"text": f'By : {Name}'},
                            }]
                    ds = requests.post(urlsf,json=datatg)
                except:pass
        else:
            count += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f"Started > | Att : {count}")
        
threads = []
for i in range(thread):
    thread2 = threading.Thread(target=r)
    thread2.start()
