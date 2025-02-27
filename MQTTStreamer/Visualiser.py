import pandas as pd
import matplotlib.pyplot as plt

file = 'MQTTStreamer\\Resources\\dati_macchina.csv'
data = pd.read_csv(file)

plt.bar(data["nome_parametro"], data["valore"])
plt.xlabel("Nome parametro")
plt.ylabel("Valore")
plt.title("Bar Graph")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

print('Fine programma')