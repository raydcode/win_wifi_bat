import subprocess
import re

def getWifiInfo():
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'network'], shell=True).decode()
    data = result.split('\n')
    ssid = [i.split(":")[1][1:-1] for i in data if "SSID" in i]
    signal = [i.split(":")[1][1:-1] for i in data if "Signal" in i]
    print("Wi-Fi Name: " + ssid[0])
    print("Signal Strength: " + signal[0] + "%")

def getBatteryInfo():
    result = subprocess.check_output(['powercfg', '/getactivescheme'], shell=True).decode()
    match = re.search("GUID: (.+)\n", result)
    power_plan_guid = match.group(1)
    result = subprocess.check_output(['powercfg', '/query', power_plan_guid], shell=True).decode()
    if "Balanced" in result:
        print("Power saving mode: Balanced")
    elif "Power saver" in result:
        print("Power saving mode: Power saver")
    else:
        print("Power saving mode: High performance")
        
        
        
        
getBatteryInfo()
getWifiInfo()