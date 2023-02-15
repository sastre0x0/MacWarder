#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig", shell=True)

inter = input("interface > ")
sp_mac = input("your new MAC > ")

print("[+] " + inter + " " + "MAC address will be changed for" + " " + sp_mac)
subprocess.call("ifconfig " + inter + " down", shell=True)
subprocess.call("ifconfig " + inter + " hw ether " + sp_mac, shell=True)
subprocess.call("ifconfig " + inter + " up", shell=True)
print("Done, thanks for your preference :)")