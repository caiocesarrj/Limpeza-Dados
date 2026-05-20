import pandas as pd
import numpy as np


df = pd.read_csv(r'C:\Projetos\Limpeza-Dados\DadosBrutos\pedidos_raw.csv')

df = df.drop_duplicates(subset='id_pedido', keep='first') # Remove duplicatas

#Conversões
df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce').astype('Int64') # Quantidade de Float para Int
df['data_pedido'] = pd.to_datetime(df['data_pedido'], format='mixed', errors='coerce') # Convertendo Data de STR pra Date e ordenando


print(df.dtypes)
print(df.head(10))





