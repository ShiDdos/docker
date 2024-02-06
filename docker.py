from colorama import *
import optparse
import datetime
from scanlib import socialmedia
from scanlib import scanwebsite
from scanlib import bitcoin
from scanlib import contact
from scanlib import compete
import requests
import socket 
import os
def banner():
    print(Fore.BLUE+f"""
                           
 ____          _           
|    \ ___ ___| |_ ___ ___ 
|  |  | . |  _| '_| -_|  _|
|____/|___|___|_,_|___|_|  
                            v.1

                        [!] This OSINT Tool created and developed by ShiDdos
    """)

def start(username,time):
    os.system('cls' if os.name=='nt' else 'clear')
    banner()    
    print(Fore.RED+f"""
    Contact :

    Github  : https://github.com/ShiDdos
    Youtube : https://www.youtube.com/@shiddos
    Discord : shiddos
    """)
    print(Fore.BLUE+f"\nStarting DOCKER OSINT scanner... ( https://github.com/ShiDdos/DOCKER ) Time : {time}")
    socialmedia.scan(username)
    scanwebsite.scan(username)
    bitcoin.scan(username)
    contact.scan(username)
    compete.scan(username)
    print(f"""

    [+] {Fore.RED}Thanks You to use {Fore.BLUE}project docker. Dont forget to star and watch to get updates annoucements.
    """)

def main():
    time= datetime.datetime.now()
    parser = optparse.OptionParser(f" sudo python3 docker.py --u username")

    parser.add_option("-u","--u",dest = "username",type="string") # username parameter
    (options,args) = parser.parse_args()
    username = options.username
    if(username == None ):
        username = input(Fore.BLUE+"[+] Username : ")
    start(username,time)


if __name__ == "__main__":
    main()
