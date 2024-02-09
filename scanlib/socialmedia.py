import requests 
from colorama import Fore
import scanlib.githubscrape as githubscrape

udata = [
    "https://github.com/{}",  # 1
    "https://instagram.com/{}",  # 2
    "https://twitter.com/{}",  # 3
    "https://t.me/{}",  # 4
    "https://{}.tumblr.com/",  # 5
    "https://www.pinterest.com/{}",  # 6
    "https://vk.com/{}",  # 7
    "https://www.reddit.com/user/{}",  # 8
    "https://mix.com/{}",  # 9
    "https://www.facebook.com/{}",  # 10
    "https://bionluk.com/{}",  # 11
    "https://gitlab.com/{}",  # 12
    "https://www.tiktok.com/@{}",  # 13
    "https://www.quora.com/{}",  # 14
    "https://medium.com/@{}",  # 15
    "https://digg.com/@{}",  # 16
    "https://www.linkedin.com/in/{}",  # 17
    "https://www.deviantart.com/{}",  # 18
    "https://www.twitch.tv/{}"  # 19	
]

sdata = [
    "status",  # 1 
    "status",  # 2
    "status",  # 3
    "status",  # 4
    "status",  # 5
    "status",  # 6
    "status",  # 7
    "https://www.reddit.com/user/admwkdamwkdamwkawd",  # 8
    "https://mix.com/",  # 9
    "status",  # 10
    "status",  # 11
    "https://gitlab.com/users/sign_in",  # 12
    "status",  # 13
    "status",  # 14
    "status",  # 15
    "status",  # 16
    "status",  # 17
    "status",  # 18
    "status"  # 19
]

def scan(username):
    print(Fore.BLUE + "Social Media Scan :\n")
    
    for i in range(len(udata)):
        url = udata[i].format(username)
        if sdata[i] == "status":
            r = requests.get(url)
            if r.status_code == 200:
                print(Fore.GREEN + f"[+] User Found : {url}")
            else:
                print(Fore.RED + f"[-] Not Found  : {url}")
        else:
            r1 = requests.get(url).text
            r2 = requests.get(sdata[i]).text
            if r1 == r2:
                print(Fore.GREEN + f"[+] User Found  : {url}")
            else:
                print(Fore.RED + f"[-] Not Found  : {url}")
    
    print(Fore.BLUE + "\nPotantial Data : ")
    print(Fore.BLUE + "Data from Github : ")
    githubscrape.getinfo(username)

# Kullanım örneği:
# scan("kullanici_adi")
