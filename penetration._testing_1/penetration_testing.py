# Library for asynchronously executing functions
# The TreadPoolExecutor does the asynchonous execution with threads
from concurrent.futures import ThreadPoolExecutor   
# Library for working with sockets. We will use it to attempt to form a TCP/IP connection
import socket
# Library for working with time. We will use it to calculate how long the application took to run 
import time
# Port 53: Standard DNS port. Critical for internet connectivity
# Port 80: Used for unencrypted HTTP(web communication)
# Port 443: Defaulty TCP for HTTPS(Secure)
# Port 8000: Alternative for HTTP

MAX_WORKERS = 100

def generate_port_list(port_range):
    """Generates a list of all ports in the range (inclusive of the last port)."""
    # The range function is end-exclusive, so we add 1 to include the last port
    return list(range(port_range[0], port_range[1] + 1)) 

def scan(ip, port, timeout=0.5):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        # connect_ex returns 0 if the connection succeeds (port is open)
        result = sock.connect_ex((ip, port))
        sock.close()
        return (port, result == 0)   # True = open
    except Exception: # Catching a generic Exception for robustness
        return (port, False)

def main():
    ip_address = "192.168.1.1"
    # Port range is (start, end). Scanning 10001 ports (0 through 10000)
    port_range = (0, 20000) 
    
    # 1. Generate a list of all individual ports
    all_ports = generate_port_list(port_range)
    total_ports_to_scan = len(all_ports)

    # Start the timer
    start_time = time.time()

    open_ports = []
    
    # 2. Use map() to correctly execute scan(ip, port) for every port
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # map() passes one item from the IP list and one item from the port list
        # for each thread: scan(ip_address, port_0), scan(ip_address, port_1), etc.
        scan_results = executor.map(scan, [ip_address] * total_ports_to_scan, all_ports)
        
        # Collect and process results
        for port, is_open in scan_results:
            if is_open:
                open_ports.append(port)

    # Finish the timer
    end_time = time.time()
    
    # 3. Print the summary with the corrected f-string
    print(f"Scanned {total_ports_to_scan} ports in {end_time - start_time:.2f} seconds.")
    print(f"Open ports found: {open_ports}")

# 4. Correct placement of the script entry point
if __name__ == "__main__":
    main()


        