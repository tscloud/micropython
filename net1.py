import network
import esp

def connect():
    # this can be run from the REPL as well
    esp.osdebug(None)   # kill all on start

    network.WLAN(network.STA_IF).active(False)
    network.WLAN(network.AP_IF).active(False)
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.config(dhcp_hostname='ESP8266_1')
        sta_if.connect('gopats', '15courthouselane')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

# call the connect() func to connect
connect()