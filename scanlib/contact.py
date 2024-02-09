import requests
from colorama import Fore

udata = [
    "https://ask.fm/{}",  # 1
    "https://www.bikemap.net/en/u/{}/routes/created/",  # 2
    "https://forum.dangerousthings.com/u/{}/summary",  # 3
    "https://forums.envato.com/u/{}",  # 4
    "https://www.cracked.com/members/{}",  # 5
    "https://ask.fedoraproject.org/u/{}",  # 6
    "https://community.cryptomator.org/u/{}",  # 7
    "https://forum.ionicframework.com/u/{}",  # 8
    "https://discourse.joplinapp.org/u/{}",  # 9
    "https://forum.rclone.org/u/{}",  # 10
    "https://forum.sublimetext.com/u/{}",  # 11
    "https://discourse.wicg.io/u/{}",  # 12
    "https://bionluk.com/{}",  # 13
    "https://www.warriorforum.com/members/{}-1.html",  # 14
]
sdata = [
    "status",  # 1
    "status",  # 2
    "status",  # 3
    "status",  # 4
    "status",  # 5
    "status",  # 6
    "status",  # 7
    "status",  # 8
    "status",  # 9
    "status",  # 10
    "status",  # 11
    "status",  # 12
    "status",  # 13
    "status",  # 14
]

def scan(username):
    print(Fore.BLUE+f"""
    
    Contact & Forum Websites Scan : 

    """)
    for i in range(len(udata)):
        if sdata[i] == "status":
            url = udata[i].format(username)
            r = requests.get(url)
            if r.status_code == 200: 
                print(Fore.GREEN+f"[+] User Found : {url}")
            else:
                print(Fore.RED+f"[-] Not Found  : {url}")
        else:
            url = udata[i].format(username)
            r1 = requests.get(url).text
            r2 = requests.get(sdata[i]).text
            if r1 == r2:
                print(Fore.GREEN+f"[+] User Found  : {url}")
            else:
                print(Fore.RED+f"[-] Not Found  : {url}")
