import psutil
import pwd

def get_telnet_sessions():
    results = []
    for conn in psutil.net_connections(kind="tcp"):
        if not conn.laddr:
            continue

        if (conn.laddr.port == 23) or (conn.raddr and conn.raddr.port == 23):
            results.append(conn)

    return results


if __name__ == "__main__":
    sessions = get_telnet_sessions()

    if not sessions:
        print("No active Telnet sessions detected.")
        exit()

    print(f"[+] Active Telnet Sessions Found: {len(sessions)}\n")

    for conn in sessions:
        try:
            user = pwd.getpwuid(conn.pid).pw_name if conn.pid else "?"
        except:
            user = "?"

        l = f"{conn.laddr.ip}:{conn.laddr.port}"
        r = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"

        print("---------------------------------------")
        print(f"PID:      {conn.pid}")
        print(f"User:     {user}")
        print(f"Local:    {l}")
        print(f"Remote:   {r}")
        print(f"Status:   {conn.status}")
    print("---------------------------------------")
