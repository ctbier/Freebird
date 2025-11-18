
# To observe established TCP connections using Python, the psutil library is a common and effective choice. # This library provides a cross-platform interface for retrieving information on running processes and 
# system utilization, including network connections.
# 11/17/2025: raise AccessDenied(pid, name) from err

import psutil

def get_established_tcp_connections():
    """
    Retrieves a list of established TCP connections on the system.
    """
    connections = []
    for conn in psutil.net_connections(kind='tcp'):
        if conn.status == psutil.CONN_ESTABLISHED:
            connections.append(conn)
    return connections

if __name__ == "__main__":
    established_conns = get_established_tcp_connections()

    if established_conns:
        print("Established TCP Connections:")
        for conn in established_conns:
            # conn.laddr: local address (ip, port)
            # conn.raddr: remote address (ip, port)
            # conn.pid: process ID associated with the connection
            print(f"  Local: {conn.laddr.ip}:{conn.laddr.port} "
                  f"-> Remote: {conn.raddr.ip}:{conn.raddr.port} "
                  f"(PID: {conn.pid if conn.pid else 'N/A'})")
    else:
        print("No established TCP connections found.")
