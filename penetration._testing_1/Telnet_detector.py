import psutil
import datetime
import getpass

# Optional: simple color output (can remove if undesired)
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

def get_telnet_sessions():
    print(f"{CYAN}[*] Telnet Session Scan — {datetime.datetime.now()}{RESET}")
    print(f"[*] Running as user: {getpass.getuser()}\n")

    telnet_sessions = []

    for conn in psutil.net_connections(kind="tcp"):
        try:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"

            # Filter Telnet (Port 23)
            if conn.raddr and conn.raddr.port == 23 or (conn.laddr and conn.laddr.port == 23):
                session_info = {
                    "pid": conn.pid,
                    "status": conn.status,
                    "local": laddr,
                    "remote": raddr,
                    "user": None,
                }

                # Try to get username
                try:
                    if conn.pid:
                        session_info["user"] = psutil.Process(conn.pid).username()
                except (psutil.AccessDenied, psutil.NoSuchProcess):
                    session_info["user"] = "Access Denied"

                telnet_sessions.append(session_info)

        except psutil.AccessDenied:
            # Ignore silently — normal without sudo
            continue
        except psutil.NoSuchProcess:
            continue

    # Output results
    if not telnet_sessions:
        print(f"{RED}[!] No active Telnet sessions detected.{RESET}")

        # Also help the user if they ran without sudo
        if getpass.getuser() != "root":
            print(f"{CYAN}[*] Hint: Run with sudo to see ALL telnet sessions:\n    sudo python3 script.py{RESET}")
        return

    print(f"{GREEN}[+] Active Telnet Sessions Found: {len(telnet_sessions)}{RESET}\n")

    for s in telnet_sessions:
        print(f"{CYAN}---------------------------------------{RESET}")
        print(f"PID:      {s['pid']}")
        print(f"User:     {s['user']}")
        print(f"Local:    {s['local']}")
        print(f"Remote:   {s['remote']}")
        print(f"Status:   {s['status']}")
    print(f"{CYAN}---------------------------------------{RESET}")


if __name__ == "__main__":
    get_telnet_sessions()
