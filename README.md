[中文说明](README_CN.md)

# web

Matter Dishwasher controller web on Raspberry Pi

## Preparations

1. Raspberry Pi: Put the chip-tool-1.2 file in the directory ~/apps.
2. Raspberry Pi: The first run must first install the bottle, execute`pip3 install bottle`
3. Raspberry Pi: `cd ~`
4. Raspberry Pi: clone this Git repository
5. Raspberry Pi: `cd ~/web`
6. Raspberry Pi: `python3 main.py`
7. Raspberry Pi: Put the PAA certificate Chip-Midea-PAA-118C-Cert.der in the directory /var/paa-root-certs/
8. Check out the Raspberry Pi IP
9. Computer: Open a web browser, enter the Raspberry Pi IP at the URL, and you can display the web page Matter Test Harness (v2.8-official). Make sure that the computer and the Raspberry Pi are connected to the network.
10. Computer: Enter the URL Raspberry Pi IP: 8088, for example, 192.168.1.104:8088, open the web page Midea Dishwasher Matter Demo
11. WiFi module: Burn firmware that supports Matter dishwasher.

## Raspberry Pi controls the dishwasher

Controller: Raspberry Pi

Server: Dishwasher

Test steps:

1. Dishwasher: power on, turn on.
2. Dishwasher: Press and hold the WiFi button for 3 seconds and wait for pairing.
3. Computer: Open the demo web page, the default Node ID is 1, fill in the SSID and password of the wireless router, click [Pair], wait a minute, and the Response: pair success will be displayed if the pairing is successful.
4. Computer: Click [Power OFF] to shut down, [Power ON] to turn on,
5. Computer: Click [Start] to start, [Pause] to pause, [Cancel] to stop
6. Computer: Click [Normal], [Heavy], [Light] to select the washing mode
7. Computer: Click [Get Status] to get the dishwasher status.

## Raspberry Pi simulates a dishwasher

Controller: Raspberry Pi

Server: Raspberry Pi simulation dishwasher APP

1. Raspberry Pi: `cd ~/apps`
2. Raspberry Pi: `./chip-dishwasher-app`
3. Raspberry Pi: pairing, `./chip-tool-1.2 pairing onnetwork-long 2 20202021 3840`
4. Computer: Change the Node ID to 2.
5. Computer: Click [Power ON] to turn on, [Power OFF] to shut down, etc.