# imports
import sys, network, time

# kill all on start
network.WLAN(network.STA_IF).active(False)
network.WLAN(network.AP_IF).active(False)

# connect to WiFi LAN
def wlan_connect(essid,password,timeout=15):
    print('Network Connect:',time.localtime())
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(dhcp_hostname='especial_1')
    if not wlan.isconnected():
        wlan.connect(essid,password)
        time.sleep(0.1)
        for x in range(timeout):
            if wlan.isconnected():
                break
            time.sleep(1)
    return_value = wlan.isconnected()
    print('Network Connect:',return_value)
    print('network Config:', wlan.ifconfig())
    #print('Network Status:',wlan.status())
    return return_value