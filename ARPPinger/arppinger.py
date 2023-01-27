import argparse
from scapy.all import *
import time
import pyfiglet
import time


class ARPPing():

    ascii_banner = pyfiglet.figlet_format("ARPPİNGER")
    print(ascii_banner)

    time.sleep(5)

    def __init__(self):
        print("ARPPing initalize...")

    def get_user_input(self):
        parser_cs = argparse.ArgumentParser(description="Tool arppinger build")
        parser_cs.add_argument('-i','--ipaddress',type=str, help="IP adresi girmelisiniz!")
        args = parser_cs.parse_args()

        #print(args.ipaddress)

        if(args.ipaddress != None):
            return args
        else:
            print("ip adresini, -i argümanıyla giriniz.")



    def arp_request(self,ip):

        arp_request_packet = scapy.ARP(pdst=ip) #pdst = destination ip address
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined_packet = broadcast_packet/arp_request_packet # / sign ,combine two tool

        #dst= ff:ff:... broadcast(yayın) packet => all network
        (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)#timeout shows how long to wait
        answered_list.summary()


if __name__ == "__main__":
    arp_ping = ARPPing()
    user_input = arp_ping.get_user_input() #return args argument => user_input
    arp_ping.arp_request(user_input.ipaddress) # args will be used here

else:
    print("**************************************************"
          "*********************************************"
          "****************************************"
          "***********************************")
