#!/usr/bin/env python

import subprocess

subprocess.call("figlet MacWarder", shell=True)
subprocess.call("ifconfig", shell=True)

inter = input("interface > ")
sp_mac = input("your new MAC > e.g. 00:10:20:30:40:50 ")

print("[+] " + inter + " " + "mac address will be changed for" + " " + sp_mac)
subprocess.call("ifconfig " + inter + " down", shell=True)
subprocess.call("ifconfig " + inter + " hw ether " + sp_mac, shell=True)
subprocess.call("ifconfig " + inter + " up", shell=True)
subprocess.call("ifconfig", shell=True) 
print("Done, thanks for your preference :)")