FROM python:3.12-alpine

RUN pip install --no-cache-dir "paho-mqtt>=2.0"

COPY solax_battery_mqtt.py /
CMD ["python3", "/solax_battery_mqtt.py"]
