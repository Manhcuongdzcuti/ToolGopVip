den = '[1;90m'
luc = '[1;32m'
trang = '[1;37m'
red = '[1;31m'
vang = '[1;33m'
tim = '[1;35m'
lamd = '[1;34m'
lam = '[1;36m'
purple = '[35m'
hong = '[1;95m'
xnhac = '[1;95m'
xduong = '[1;95m'
do = '[1;33m'
import requests,os,sys, time
import requests
import json
import os
from sys import platform
from datetime import datetime
from time import sleep, strftime
import hashlib
import hmac
import uuid
ctool1 = "\033[1;32m[\033[1;33m✓\033[1;32m] \033[1;0m=> "
ctool2 = "\033[1;0m➲ "
try:
    from pystyle import Colors, Colorate
except ImportError:
    os.system('pip install pystyle')
    from pystyle import Colors, Colorate
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\033[1;31mBạn Định Bug À, Có Cái Lồn!")
    exit() 

banners = f"""      ██████╗         ████████╗ ██████╗  ██████╗ ██╗
     ██╔════╝         ╚══██╔══╝██╔═══██╗██╔═══██╗██║
     ██║       █████╗    ██║   ██║   ██║██║   ██║██║
     ██║       ╚════╝    ██║   ██║   ██║██║   ██║██║
     ╚██████╗            ██║   ╚██████╔╝╚██████╔╝███████╗
      ╚═════╝            ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝"""

thongtin = f"""                       \033[1;37mCopyright © C-Tool 2024\n\033[1;32m─────────────────────────────────────────────────────────────────\n\033[1;32m[\033[1;0m🌃\033[1;32m]\033[1;37m ➩ {Colorate.Horizontal(Colors.yellow_to_red, 'Tool: Gộp Vip')}\n\033[1;32m[\033[1;0m🌃\033[1;32m]\033[1;37m ➩\033[1;35m Admin: \033[1;36mCao Mạnh Cường  \n\033[1;32m[\033[1;0m🌃\033[1;32m]\033[1;37m ➩\033[1;36m Zalo: \033[1;31m0365232190\n\033[1;32m[\033[1;0m🌃\033[1;32m]\033[1;37m ➩\033[1;32m Box TeleGram: \033[1;37mhttps://t.me/+lgM50Gu-4Ns1ZTJl\n\033[1;32m[\033[1;0m🌃\033[1;32m]\033[1;37m ➩\033[1;33m YouTube: \033[1;37mhttps://youtube.com/@Manhcuongdzcuti\n\033[1;32m[\033[1;0m🌃\033[1;32m]\033[1;37m ➩ {Colorate.Horizontal(Colors.green_to_white, 'Mua Key Tại: ')}{Colorate.Horizontal(Colors.white_to_green, 'Chưa Cập Nhật  ')}\n\033[1;32m─────────────────────────────────────────────────────────────────\033[0m
"""

def vanlong(so):
    a = '\033[1;32m────' * (so - 1) + '─'
    for i in range(len(a)):
        sleep(0.003)
    print(a)

def clear():
    if platform.startswith('linux'):
        os.system('clear')
    else:
        os.system('cls')

def banner():
    print('[0m', end='')
    clear()
    a = Colorate.Horizontal(Colors.blue_to_green, banners)
    print(a)
    print(thongtin)
    vanlong(17)
os.system("cls" if os.name == "nt" else "clear")
banner()
print("\033[1;31mTool Đang Bảo Trì!")
print(f"{ctool2}\033[1;32mNhập [\033[1;33m1\033[1;32m] Để Out Tool")
chon = float(input('\033[1;0m═══➲ \033[1;32mTNhập Số \033[1;0m===>: \033[1;33m'))
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\n\033[1;31mBạn Định Bug À?, Cốn Cái Lò!")
    sys.exit(1) 
if chon == 1 :
  print("\033[1;32mThoát Tool Trong 3s Nữa!")
  sleep(3)
  exit()
  
