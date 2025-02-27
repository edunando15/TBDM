import pandas as pd
import paho.mqtt.client as mqtt
from time import sleep
import json

# Read CSV file:
csv_file = 'MQTTStreamer\\Resources\\dati_macchina_copy.csv'
data_frame = pd.read_csv(csv_file)

# Define parameters to connect to MQTT broker.
broker = 'localhost'
port = 1883
topic = 'test-topic'

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker, port)

for index, row in data_frame.iterrows():
    # Convert row serie to dictionary.
    row_dict = row.to_dict()
    # Serialize dictionary to JSON.
    payload = json.dumps(row_dict)
    client.publish(topic, payload)
    sleep(1)