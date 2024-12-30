from socket import *
import sys

# Function to scan a single port
def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print(f'[+] Port {tgtPort} is open')
        connskt.close()
    except:
        pass  # If the connection fails, do nothing (port is closed)

# It's a function to perform a port scan on a given host and list of ports
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)  # Gets the IP address of the target host
    except:
        print(f'[-] Cannot resolve {tgtHost}')
        return

    try:
        tgtName = gethostbyaddr(tgtIP)  # Gets the name of the target host (basically reverse DNS)
        print(f'\n[+] Scan result for: {tgtName[0]}')
    except:
        print(f'\n[+] Scan result for: {tgtIP}')

    setdefaulttimeout(1)  # Sets a timeout for connections
    open_ports = []  # List to store open ports

    for tgtPort in tgtPorts:
        print(f'Scanning port {tgtPort}...')
        conScan(tgtHost, tgtPort)

def get_ports_from_user():
    # Asks the user for a list of ports to scan
    ports_input = input("Enter a list of ports to scan (comma separated, e.g., 80, 443, 22): ")
    ports = ports_input.split(',')

    # Convert ports to integers
    try:
        ports = [int(port.strip()) for port in ports]
    except ValueError:
        print("[-] Invalid port number(s). Please ensure all ports are integers.")
        sys.exit(1)

    return ports

if __name__ == '__main__':
    tgtHost = input("Enter the host to scan (e.g., google.com): ").strip()
    ports = get_ports_from_user()

    # Starts the port scan
    print(f"\nStarting scan on {tgtHost} for ports: {ports}")
    portScan(tgtHost, ports)
