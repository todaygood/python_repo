#!/usr/bin/env python

import netifaces
import sys
import os

def get_interface(ip_addr):
    nics = netifaces.interfaces()
    for nic in nics:
        info = netifaces.ifaddresses(nic)
        addr = info.get(2)
        if addr and ( addr[0]['addr'] == ip_addr):
            return nic

    return None


if __name__ == "__main__":
    if len(sys.argv) < 4 :
        print("Usage: %s bond0.<vlan_id>  br1  ip")
        exit(1)

    bond= sys.argv[1]
    bridge = sys.argv[2]
    ip_addr = sys.argv[3]

    interface = get_interface(ip_addr)
    if interface == bond :
        os.execl("/usr/sbin/ifdown","/usr/sbin/ifdown",interface)
    elif interface == bridge:
        print("It has been ok.")
    else:
        print("arg is wrong, please check!")


