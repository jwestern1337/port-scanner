#-------------------------------------------------------------------------------
# Name:        portscanner.py
# version:     1.2
#
# Developer:   Jack western
#
# Created:     07/03/2022
# Licence:     Open Source
#-------------------------------------------------------------------------------

import sys, socket, threading, requests
from rich import print

print("""
██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║   ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║   ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
""")

try:
    a = requests.post('https://www.google.com')
    if a.status_code != 405:
        print("You are not connected to the internet") # quick interent check
    else:
        pass
except Exception as e:
    print(e)

def main():
    host = input("Enter an address to scan: ")
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Failed to conver domain to IP, please do it manually")
    print('=' * 80)
    if host != ip:
        print(f'Scanning [bold]{host}[/bold] ([bold]{ip}[/bold]) on 65535 ports')
        scan_ports(ip, delay=3)
    else:
        print(f'Scanning [bold]{host}[/bold] on 65535 ports')
        scan_ports(ip, delay=3)


def try_port(ip, port, delay, open_ports):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(delay)
    result = sock.connect_ex((ip, port))

    if result == 0: 
        open_ports[port] = 'open'
        return True
    else:
        open_ports[port] = 'closed'
        return None

threads = []
open_ports = {}
def scan_ports(ip, delay):
    for port in range(0, 65535):
        thread = threading.Thread(target=try_port, args=(ip, port, delay, open_ports))
        threads.append(thread)

    for i in range(0, 65535):
        threads[i].start()

    for i in range(0, 65535):
        threads[i].join()

    for i in range (0, 65535):
        if open_ports[i] == 'open':
            print('port number ' + str(i) + ' is open')
        if i == 65535:
            print('\nscan complete!')


try:
    if len(sys.argv[1]) < 1:
        main()
    else:
        try:
            ip = socket.gethostbyname(sys.argv[1])
        except socket.gaierror:
            print("Failed to conver domain to IP, please do it manually")
        print('=' * 80)
        if sys.argv[1] != ip:
            print(f'Scanning [bold]{sys.argv[1]}[/bold] ([bold]{ip}[/bold]) on 65535 ports')
        else:
            print(f'Scanning [bold]{sys.argv[1]}[/bold] on 65535 ports')
        scan_ports(ip=sys.argv[1], delay=3)
        print("=" * 80)
except IndexError:
    main()
    print("=" * 80)
