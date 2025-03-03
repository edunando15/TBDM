import pandas as pd
import paho.mqtt.client as mqtt
from time import sleep
import json

host = 'localhost'
port = 1883
topic = 'new-test-topic'
date = "2025-03-02T11:00:04.792Z"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect(host, port)

data = {
    "id": "53c39422-3d7c-4220-b0cf-c79567d75b40",
    "id_macchina": "65f850b321e42e5ffa7cf088",
    "valore": 2.8,
    "data_registrazione": date,
    "createdAt": date,
    "updatedAt": date,
    "nome_parametro": "PV07_Vibrazioni",
    "tipo_dato": "number"
}

payload = json.dumps(data)

client.publish(topic, payload)