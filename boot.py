# non-blank boot.py

# connect to network
import net2
if net2.wlan_connect('gopats','15courthouselane'):
    print('network connection SUCCESS')
else:
    print('network connection FAILURE')