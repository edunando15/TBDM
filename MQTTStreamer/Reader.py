import pandas as pd
import paho.mqtt.client as mqtt
from time import sleep

# Read CSV file:
csv_file = 'Resources\\dati_macchina.csv'
data_frame = pd.read_csv(csv_file)

# Connect to MQTT broker.
broker = 'localhost'
port = 1883
topic = 'test-topic'

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker, port)

for row in data_frame.iterrows():
    payload = str(row)
    client.publish(topic, payload)
    sleep(1)