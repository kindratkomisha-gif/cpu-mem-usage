# Cross-Platform System Monitor CLI

A lightweight, cross-platform command-line utility written in Python that monitors CPU usage and physical memory in real-time with a custom terminal loading animation.

---

##  Features

* **Cross-Platform Support:** Automatically detects your operating system (`Windows`, `Linux`, or `macOS`) and uses the appropriate native system commands.
* **Real-Time Monitoring:** Continuously loops to fetch updated CPU load and memory statistics.
* **Visual Loading Bar:** Features a smooth terminal-based progress animation for each refresh cycle.
* **Memory Calculation:** Automatically parses raw system outputs and formats memory values into readable Megabytes (MB).

---

##  Requirements & System Commands

The script relies on built-in OS utilities to fetch hardware metrics without requiring third-party Python packages (like `psutil`):

* **Windows:** Uses PowerShell (`Get-CimInstance`) to query `Win32_Processor` and `Win32_OperatingSystem`.
* **Linux:** Uses `top` and `free` utilities.
* **macOS:** Uses built-in `top` utility commands.

---
