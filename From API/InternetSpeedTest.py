import os
import speedtest

os.system('clear')
print("\033[4mConnecting...\033[0m")
st = speedtest.Speedtest()

os.system('clear')
print("\033[4mTesting download...\033[0m")
print("Download: ", end="")
dl = round(st.download() / 1000000, 2)
print(dl, "MBit/s")

os.system('clear')
print("\033[4mTesting upload...\033[0m")
print("Download:", dl, "MBit/s")
print("Upload: ", end="")
ul = round(st.upload() / 1000000, 2)
print(ul, "MBit/s")

os.system('clear')
print("\033[4mTesting PING...\033[0m")
print("Download:", dl, "MBit/s")
print("Upload:", ul, "MBit/s")
print("PING: ", end="")
server_names = []
st.get_servers(server_names)
ping = st.results.ping
print(ping, "ping")

os.system('clear')
print("\033[4mTest complete.\033[0m")
print("Download:", dl, "MBit/s")
print("Upload:", ul, "MBit/s")
print("PING:", ping, "ping")
