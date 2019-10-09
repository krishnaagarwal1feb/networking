#!/usr/bin/env python 
#"provide the interface and mac address in command line"
import subprocess
import argparse
import sys

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for" + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig",interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig",interface, "up"])

change_mac(sys.argv[1], sys.argv[2])
    
