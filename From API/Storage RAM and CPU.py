import psutil
import os

cpu = "Calculating..."

while 1:

    try:

        os.system('clear')

        print("CTRL+C (^C) to exit. ")

        hdd = psutil.disk_usage('/')

        giga = 1000 ** 3

        print("\nStorage on disk:")
        print(f"Total: {round(hdd.total / giga, 2)} GB")
        print(f"Used: {round(hdd.used / giga, 2)} GB")
        print(f"Free: {round(hdd.free / giga, 2)} GB")

        giga = 1024 ** 3

        print("\nMemory (RAM):")
        print(f"Total: {round(psutil.virtual_memory().total / giga, 2)} GB")
        print(f"Available: {round(psutil.virtual_memory().available / giga, 2)} GB")
        print(f"Percentage used: {round(psutil.virtual_memory().percent, 2)}%")

        print("\nCPU:")
        print(f"Running at {cpu}%")

        cpu = psutil.cpu_percent(1)

    except KeyboardInterrupt:

        print("\nExiting...")
        break
