import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import sys
import os

root.geometry("1000x700")


# Path to the privileged helper script
HELPER = os.path.join(os.path.dirname(__file__), "telnet_scan_helper.py")

def run_scan():
    """
    Run the privileged scan helper using sudo and show results in GUI.
    """

    # Clear old text
    output_box.delete(1.0, tk.END)

    # Command to run helper with sudo
    cmd = ["sudo", sys.executable, HELPER]

    try:
        # Ask for sudo password in macOS GUI-friendly way
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        out, err = proc.communicate()

        if err:
            output_box.insert(tk.END, f"[ERROR]\n{err}\n")
        if out:
            output_box.insert(tk.END, out)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------- GUI WINDOW ----------
root = tk.Tk()
root.title("Telnet Session Detector")
root.geometry("700x500")

title_label = tk.Label(root, text="Telnet Session Scanner", font=("Arial", 20))
title_label.pack(pady=15)

scan_button = tk.Button(root, text="Run Scan", font=("Arial", 14), command=run_scan)
scan_button.pack(pady=10)

output_box = scrolledtext.ScrolledText(root, width=80, height=20, font=("Courier", 11))
output_box.pack(padx=10, pady=10)

root.mainloop()
