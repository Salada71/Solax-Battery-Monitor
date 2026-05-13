# Solax-Battery-Monitor

Solax T58 Battery Monitor — passive RS-485 sniffer → MQTT bridge

Passively listens to communication between the inverter (master) and batteries (slave)
on the RS-485 bus via Waveshare ETH-RS485 in transparent TCP mode.
No active queries — only reads what the inverter and batteries communicate.