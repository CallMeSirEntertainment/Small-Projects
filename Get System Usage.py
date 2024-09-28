import psutil
from os import system, name
from time import sleep
while True:
    system('cls' if name == 'nt' else 'clear')
    cpu_cores = psutil.cpu_percent(percpu=True)
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    print('CPU Usage:')
    i = 1
    for cpu_percent in cpu_cores:
        print(f"Core {i}: {cpu_percent}%")
        i += 1
    print(f"\nMemory Usage: {memory_percent}%")
    sleep(1)