import requests
from colorama import Fore

lst = [
    "http://{}.cf",
    "http://{}.tl",
    "http://{}.ml",
    "http://{}.com",
    "http://{}.org",
    "http://{}.me",
    "http://{}.info",
    "http://{}.net",
    "http://{}.online",
    "http://{}.site",
    "http://{}.tr",
    "http://{}.de",
    "http://{}.app",
    "http://{}.live",
    "http://{}.store",
    "http://{}.shop",
    "http://{}.website",
    "http://{}.xyz",
    "http://{}.plus",
    "http://{}.bet",
    "http://{}.group",
    "http://{}.io"
]

def scan(username):
    print(Fore.BLUE + """
    
    Website Domain Scan : 

    """)
    for i in range(len(lst)):
        url = lst[i].format(username)
        try:
            req = requests.get(url)
            found = True
        except requests.exceptions.RequestException as e:
            found = False

        if found:
            print(Fore.GREEN + f"[+] Website Found    : {url}")
        else:
            print(Fore.RED + f"[-] Website Not Found : {url}")

# Kullanım örneği:
# scan("kullanici_adi")
