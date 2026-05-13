@echo off
python.exe solax_battery_mqtt.py --tcp-host 192.168.X.X --tcp-port 502 --slaves 4 --mqtt-host 192.168.X.X --mqtt-user user --mqtt-password password --publish-interval 10 --debug