import random
import string
import time
import os
from time import sleep
from os import system, name
import random as rn
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("prnt.sc generator - STATUS: Turning on...")
time.sleep(0.01)
print("██████╗░██████╗░███╗░░██╗████████╗░░░░██████╗░█████╗░ ")
time.sleep(0.01)
print("██╔══██╗██╔══██╗████╗░██║╚══██╔══╝░░░██╔════╝██╔══██╗ ")
time.sleep(0.01)
print("██████╔╝██████╔╝██╔██╗██║░░░██║░░░░░░╚█████╗░██║░░╚═╝")
time.sleep(0.01)
print("██╔═══╝░██╔══██╗██║╚████║░░░██║░░░░░░░╚═══██╗██║░░██╗ ")
time.sleep(0.01)
print("██║░░░░░██║░░██║██║░╚███║░░░██║░░░██╗██████╔╝╚█████╔╝ ")
time.sleep(0.01)
print("╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝╚═════╝░░╚════╝░ ")
time.sleep(0.01)
print("                                                      ")
time.sleep(0.01)
print("░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░")
time.sleep(0.01)
print("██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
time.sleep(0.01)
print("██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝")
time.sleep(0.01)
print("██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗")
time.sleep(0.01)
print("╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║")
time.sleep(0.01)
print("░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")
time.sleep(0.5)
print(" ")
print("Welcome...Ready to see some prnt.sc links?")
time.sleep(1)
print("Let's generate them!")
ctypes.windll.kernel32.SetConsoleTitleW("prnt.sc generator - STATUS: Generating...")

print(" ")
time.sleep(1)

def get_random_string(length):
    letters = string.ascii_lowercase + string.digits
    result_str = ''.join(rn.choice(letters) for i in range(length))
    print("https://prnt.sc/" + result_str)

for i in range(200):
    get_random_string(6)
    time.sleep(0.02)

print(" ")
time.sleep(0.5)
print("Here you go!")
ctypes.windll.kernel32.SetConsoleTitleW("prnt.sc generator - STATUS: Links generated...")
time.sleep(0.5)
print(" ")
x = input("Press Enter for exit")