# Library for asynchronously executing functions
# The TreadPoolExecutor does the asynchonous execution with threads
from concurrent.futures import ThreadPoolExecutor   
# Library for working with sockets. We will use it to attempt to form a TCP/IP connection
import socket
# Library for working with time. We will use it to calculate how long the application took to run 
import time

MAX_WORKERS = 100

def generate_port_chunks(port_range):
    # Get the min and max port numbers from the port range
    port_ranges = port_range
    port_chunks = []
    # Divide the port range into chunks
    chunk_size = int((int(port_ranges[1]) - int(port_ranges[0])) / MAX_WORKERS)
    # Create a nested list of port chunks to the handled by each worker.
    for i in range(MAX_WORKERS):
        start = int(port_ranges[0]) + (i * chunk_size)
        end = start + chunk_size
        port_chunks.append([start, end])
    return port_chunks

def scan(ip, port, timeout=0.5):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return (port, result == 0)   # True = open
    except:
        return (port, False)


def main():
    ip_address = "192.168.1.1"
    port_range = (0, 10000)
    
    # Divide port range into chunks
    port_chunks = generate_port_chunks(port_range)

    # Start the timer
    start_time = time.time()

    # Submit the tasks to bew executed by the thread pool using map
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(scan, [ip_address] * len(port_chunks), port_chunks)
    # Finish the timer
        end_time = time.time()
        print(f, "Scanned {port_range[1]} ports in {end_time - start_time} seconds.")

    if __name__ == "__main__":
        main()


    

     






        