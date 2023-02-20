#!/usr/bin/env python

import subprocess
import argparse
import random

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--interface", dest="inter", help="Interface to change its MAC address")
parser.add_argument("-m", "--mac", dest="new_mac", help="MAC address you want to use (use 'r' or 'random' for random MAC address).")

args = parser.parse_args()

def change_mac():
    if not inter:
        print("No interface was selected")
    if not new_mac:
        print("No MAC address was provided")
    else:
        print("[+] " + inter + " " + "MAC address will be changed for" + " " + new_mac)
        subprocess.call(["ifconfig", inter, "down"])
        subprocess.call(["ifconfig", inter, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", inter, "up"])
        subprocess.call(["ifconfig", inter])

if args.inter and args.new_mac:
    inter = args.inter
    new_mac = args.new_mac

else:
    subprocess.call(["ifconfig"])
    inter = input("interface > ")
    new_mac = input("your new MAC > ")

if new_mac.lower() == "r" or new_mac.lower() == "random":
    new_mac = ":".join([str(hex(random.randint(0x00, 0xff)))[2:].zfill(2) for _ in range(6)])
    print("Randomly generated MAC address:", new_mac)

change_mac()


