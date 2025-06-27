# Python Network Scanner

A Python tool to scan local network IP ranges for active hosts, retrieve their MAC and IP addresses via ARP, and scan common TCP ports. Results are saved in both JSON and CSV formats.

## Features
- Scans local subnet for active devices using ARP requests
- Retrieves MAC and IP addresses of active hosts
- Scans specified TCP ports using socket connections
- Outputs results to scan_results.json and scan_report.csv

## How It Works
- Uses ARP requests to discover active devices in a subnet
- Scans each active device for specified open TCP ports
- Stores scan results in JSON and CSV files

## Requirements
- Python 3.x
- scapy library (install with `pip install scapy`)

## Usage
- Set your target IP range in the `ip_range` variable (e.g., "192.168.1.1/24")
- Define ports to scan in `ports_to_scan` (e.g., [22, 80, 443])
- Run the script:


## Notes
- Requires admin/root privileges to send ARP packets
- Use responsibly on networks you own or have permission to scan

## License
MIT License
