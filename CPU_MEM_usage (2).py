import sys
import time
import os
import subprocess

is_win = sys.platform.startswith("win")
is_linux = sys.platform.startswith("linux")
is_mac = sys.platform.startswith("darwin")

if is_win:
    clear_command = "cls"
    command_1 = ["powershell", "-Command", "Get-CimInstance -ClassName Win32_Processor | Select-Object -ExpandProperty LoadPercentage"]
    command_2 = ["powershell", "-Command", "Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object FreePhysicalMemory, TotalVisibleMemorySize"]
elif is_linux:
    clear_command = "clear"
    command_1 = ["bash", "-c", "top -bn1 | grep '%Cpu'"]
    command_2 = ["bash", "-c", "free -h"]
elif is_mac:
    clear_command = "clear"
    command_1 = ["zsh", "-c", "top -l 1 | grep 'CPU usage'"]
    command_2 = ["zsh", "-c", "top -l 1 | grep PhysMem"]
else:
    print("No such platform")


simple_loader = "|"*80
data = "Loading", "Loading"

while True:
    x = subprocess.Popen(command_1, stdout=subprocess.PIPE, text=True)
    y = subprocess.Popen(command_2, stdout=subprocess.PIPE, text=True)

    os.system(clear_command)

    print(simple_loader)
    print("Enter Ctrl+C for end program")

    print(data[0])
    print(data[1])

    for i in simple_loader:
        print(i, flush=True, end="")
        time.sleep(2/len(simple_loader))

    cpu = f"CPU load: {x.communicate()[0].strip()}%"
    memory = y.communicate()[0].strip()
    if is_win:
        memory = memory.splitlines()[2].split()
        memory = f"Free physical memory: {round(int(memory[0])/1024)} Mb | Total physical memory: {round(int(memory[1])/1024)}Mb"
    elif is_linux or is_mac:
        memory = memory.splitlines()[1].split()
        memory = f"Free physical memory: {memory[3]} Mb | Total physical memory: {memory[1]}Mb"
        
    data = [cpu, memory]