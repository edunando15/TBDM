import pandas as pd

# Read CSV file:
csv_file = 'MQTTStreamer\\Resources\\dati_macchina.csv'
data_frame = pd.read_csv(csv_file)

for index, row in data_frame.iterrows():
    if row['nome_parametro'] == 'PV32_Latitudine':
        data_frame.at[index, 'nome_parametro'] = 'latitude'
        data_frame.at[index, 'valore'] = 43.139531626449596
    elif row['nome_parametro'] == 'PV33_Longitudine':
        data_frame.at[index, 'nome_parametro'] = 'longitude'
        data_frame.at[index, 'valore'] = 13.068520549124521
    elif row['nome_parametro'] == 'PV17_UmiditàUscitaFango':
        data_frame.at[index, 'nome_parametro'] = 'PV17_UmiditaUscitaFango'
    elif row['nome_parametro'] == 'PV16_TorbiditàChiarificato':
        data_frame.at[index, 'nome_parametro'] = 'PV16_TorbiditaChiarificato'
    elif row['nome_parametro'] == 'PV15_TorbiditàFango':
        data_frame.at[index, 'nome_parametro'] = 'PV15_TorbiditaFango'

file_copy = 'MQTTStreamer\\Resources\\dati_macchina_copy.csv'
data_frame.to_csv(file_copy, index=False)