import socket
from rich import print
import os
from os import system
from datetime import datetime
from IPy import IP
system('title Port scanner - loading...')
def clear():
    if os.name == 'nt':
        system('cls')
    else:
        system('clear')
def scan(ipaddress, port, timeout):
    try:
        sock = socket.socket()
        sock.settimeout(float(timeout))
        sock.connect((ipaddress, port))
        print(f"[red][+] port {port} is open")
    except:
        pass
    print("Finished scanning!")

system('title Port scanner - menu')
target = input("Target to scan: ")
try:
    host_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("[red]Failed to convert domain/hostname to IP, please try again or enter domain/hostname IP[/red")
    input()
try:
    ports = int(input("Amount of ports to scan: "))
except ValueError:
    print("[red]Please enter a number next time[/red]")
    input()
try:
    timeout = float(input("Time to spend on each port: "))
except ValueError:
    print("[red]Please enter a number next time[/red]")
    input()
before = datetime.now()
print('-' * 80)
if target != host_ip:
    print(f'Scanning {target} ({host_ip}) on {ports} ports')
else:
    print(f'Scanning {target} on {ports} ports')
print('-' * 80)
system('title Port scanner - scanning...')
for port in range(1, ports):
    scan(host_ip, port, timeout)

input()
"""
65535 ports in total though

2160000 ports in 10 hours with a 0.001 timeout
1080000 ports in 5 hours with a 0.001 timeout
216000 ports in an hour  with a 0.001 timeout
3600 ports in 1 minute with a 0.001 timeout
600 ports in 10 seconds with a 0.001 timeout
60 ports a second with a 0.001 timeout
"""