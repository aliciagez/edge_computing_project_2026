import json 
import network
import rp2
import time

rp2.country("SE")

with open("wifi_cred.json") as file:
    credentials = json.load(file)

def connect_wifi(waiting_time=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(pm=0xa11140)

    if wlan.isconnected():
        print("Connected to wifi")
        return True

    wlan.connect(credentials.get("SSID"), credentials.get("PASSWORD"))

    while waiting_time > 0:
        if wlan.isconnected():
            print("Connected to wifi")
            print(wlan.ifconfig())
            return True

        if waiting_time % 10 == 0:
            print("Retrying connect...")
            wlan.connect(credentials.get("SSID"), credentials.get("PASSWORD"))

        waiting_time -= 1
        print("Trying to connect wifi, pls wait")
        time.sleep(1)

    return False
