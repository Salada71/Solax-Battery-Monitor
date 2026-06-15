@echo off
python.exe solax_battery_mqtt.py --tcp-host 192.168.85.198 --tcp-port 502 --slaves 4 --mqtt-host 192.168.85.142 --mqtt-user user --mqtt-password password --publish-interval 10 --debug