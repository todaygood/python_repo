#!/usr/bin/env python

import netifaces


def get_interface(ip_addr):
    nics = netifaces.interfaces()
    for nic in nics:
        info = netifaces.ifaddresses(nic)
        addr = info.get(2)
        if addr and ( addr[0]['addr'] == ip_addr):
            return nic

    return None


if __name__ == "__main__":
    interface = get_interface("192.168.172.129")
