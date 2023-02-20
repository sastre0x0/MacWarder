import subprocess
import argparse
import random
import re

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--interface", dest="inter", help="Interface to change its MAC address")
parser.add_argument("-m", "--mac", dest="new_mac", help="MAC address you want to use (use 'r' or 'random' for random MAC address).")

args = parser.parse_args()

def change_mac():
    inter = args.inter
    new_mac = args.new_mac
    if not inter:
        print("No interface selected")
    if not new_mac:
        print("No MAC address provided")
    else:
        print("[+] " + inter + " " + "MAC address will be changed for" + " " + new_mac)

        current_mac = get_mac_address(inter)
        print("[+] Current MAC address is", current_mac)

        subprocess.call(["ifconfig", inter, "down"])
        subprocess.call(["ifconfig", inter, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", inter, "up"])

        new_mac = get_mac_address(inter)
        if new_mac == current_mac:
            print("[-] Failed to change MAC address")
        else:
            print("[+] MAC address was successfully changed to", new_mac)

def get_mac_address(inter):
    output = subprocess.check_output(["ifconfig", inter], stderr=subprocess.DEVNULL)
    match = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    if match:
        return match.group(0)
    else:
        raise ValueError("Could not find MAC address for interface")

if args.inter and args.new_mac:
    if args.new_mac.lower() == "r" or args.new_mac.lower() == "random":
        args.new_mac = ":".join([str(hex(random.randint(0x00, 0xff)))[2:].zfill(2) for _ in range(6)])
        print("Randomly generated MAC address:", args.new_mac)

    change_mac()

else:
    subprocess.call(["ifconfig"])
    inter = input("interface > ")
    new_mac = input("your new MAC > ")
    if new_mac.lower() == "r" or new_mac.lower() == "random":
        new_mac = ":".join([str(hex(random.randint(0x00, 0xff)))[2:].zfill(2) for _ in range(6)])
        print("Randomly generated MAC address:", new_mac)

    args.inter = inter
    args.new_mac = new_mac

    change_mac()
