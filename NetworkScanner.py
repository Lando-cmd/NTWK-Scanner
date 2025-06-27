import scapy.all as scapy
import socket
import json
import csv


# Identify active devices on the network
def scan_network(ip_range):
    active_devices = []
    # Sends ICMP requests to devices in the IP range
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    for element in answered_list:
        active_devices.append({"ip": element[1].psrc, "mac": element[1].hwsrc})

    return active_devices


# Scan for open ports on a device
def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


# Saves the results to a file
def save_results(active_devices, filename="scan_results.json"):
    with open(filename, 'w') as file:
        json.dump(active_devices, file, indent=4)


# Generates a report
def generate_report(active_devices, filename="scan_report.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['IP Address', 'MAC Address', 'Open Ports']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for device in active_devices:
            writer.writerow({
                'IP Address': device['ip'],
                'MAC Address': device['mac'],
                'Open Ports': ', '.join(map(str, device['open_ports'])) if 'open_ports' in device else 'None'
            })


# Example Usage
ip_range = "000.000.0.0/00"  # Modify as needed
ports_to_scan = [00, 00, 000, 0000]  # Modify as needed

active_devices = scan_network(ip_range)

for device in active_devices:
    open_ports = scan_ports(device['ip'], ports_to_scan)
    device['open_ports'] = open_ports

save_results(active_devices)
generate_report(active_devices)
