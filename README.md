Features
-Scans local network IP range for active hosts
-Retrieves MAC and IP addresses using ARP requests
-Scans for common open ports using TCP socket connections
-Outputs results to both JSON and CSV formats

How It Works
Uses ARP requests to identify active devices within a given subnet
Scans each active device for specified TCP ports
Stores results in scan_results.json and scan_report.csv

Requirements
Python 3.x

scapy
To install required libraries, run:
pip install scapy

Usage
Edit the script as needed:

Set your target IP range in the ip_range variable (e.g., "192.168.1.1/24")

Define the list of ports to scan in ports_to_scan (e.g., [22, 80, 443])

Then run the script:
python NetworkScanner.py

Notes
Requires administrative/root privileges to send ARP packets

Use responsibly on networks you own or have permission to scan

License
This project is open-source and available under the MIT License.
