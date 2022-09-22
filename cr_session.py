from telethon import TelegramClient,sync
from telethon import functions, types
from colorama import Fore
from telethon.errors.rpcerrorlist import *
from telethon.errors import *
import os
#Bảng màu
R = Fore.RED 
B = Fore.BLUE
G = Fore.GREEN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
C = Fore.CYAN
BA = Fore.BLACK
api_id = 2182338
api_hash = 'fa411eff2ec7dcf61bdfadd2478e07bb'
if not os.path.exists("session"):
   os.makedirs("session")
def session():
    print(Y+"Input phone")
    phone = input("Nhập số điện thoại (+84582123442): "+M)
    client = TelegramClient("session/"+phone,api_id,api_hash)
    client.connect()
    if not client.is_user_authorized():
        try:
            client.send_code_request(phone)
            client.sign_in(phone,input(M+"Code login : "))
            print(G+"Create success session")
            print("Tạo thành công session "+Y+phone)
            with open("list.txt","a") as file:
                file.write(phone+"\n")
        except SessionPasswordNeededError:
            client.start(phone,input(M+'Password 2FA: '))
            print(G+"Create success session")
            print("Tạo thành công session "+Y+phone)
            with open("list.txt","a") as file:
                file.write(phone+"\n")
        except Exception as e:
            print(R,e," ",phone)
        client.disconnect()
    else:
        print(B+"Session has been created ")
        print("Session đã tạo từ trước "+phone)
        client.disconnect()
    print(C+"="*40)
while(True):
    session()