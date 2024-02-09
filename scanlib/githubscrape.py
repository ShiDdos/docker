import json
import requests
from colorama import Fore
import scanlib.js as js

def getinfo(username):
    url = "https://api.github.com/users/{}".format(username)

    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP hata durumunu kontrol et

        data = response.json()
        js.jsd("error", data)

        need = [
            'name',
            'type',
            'company',
            'location',
            'email'
        ]

        user_data = js.pdata(need, data)
        print(json.dumps(user_data, indent=True))

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Error fetching data for user {username}: {e}")

# Kullanım örneği:
# getinfo("kullanici_adi")
