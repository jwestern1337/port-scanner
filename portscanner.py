import socket, threading
from rich import print

host = input("Enter an address to scan: ")
try:
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Failed to conver domain to IP, please do it manually")
print('=' * 80)
if host != ip:
    print(f'Scanning {host} ({ip}) on 65535 ports')
else:
    print(f'Scanning {host} on 65535 ports')
threads = []
open_ports = {}

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

if __name__ == "__main__":
    scan_ports(ip, 3)
    print('=' * 80)
