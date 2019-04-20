
import psutil


def get_interface(management_ip):
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for item in v:
            if item[0] == 2 and item[1] == management_ip:
                print("interface is " + k)
                return k


if __name__ == "__main__":
    interface = get_interface("192.168.172.129")


