#!/usr/bin/python3
import os
import requests
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    os.system("figlet test")
    os.system("clear")
except:
    os.system("apt-get install figlet")

def banner():
    os.system("figlet ClickJacker")
    print("----------------"*3)
    print("")



now = datetime.now()
current_time = now.strftime("%H:%M:%S")
banner()

URL=input(bcolors.OKGREEN+"Target URL: "+bcolors.WARNING)
print(bcolors.ENDC+"")

site = URL
headers = requests.get(site).headers


try:
    print(headers["X-Frame-Options"])
    os.system("clear")
    banner()
    print(current_time+"  "+URL+"  "+bcolors.OKGREEN+"No clickjacking vulnerability detected"+bcolors.ENDC)
    print("")
    print("Current Headers: "+bcolors.OKGREEN)
    print(headers)
    print(""+bcolors.ENDC)

except:
    print(current_time+"  "+URL+"  "+bcolors.FAIL+"Vulnerable to clickjacking !"+bcolors.ENDC)
    print("")
    print("Current Headers: "+bcolors.OKGREEN)
    print(headers)
    print(""+bcolors.ENDC)

