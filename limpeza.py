import pandas as pd
import numpy as np


df = pd.read_csv(r'C:\Projetos\Limpeza-Dados\DadosBrutos\pedidos_raw.csv')

df = df.drop_duplicates(subset='id_pedido', keep='first') # Remove duplicatas

#Conversões
df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce').astype('Int64') # Quantidade de Float para Int
df['data_pedido'] = pd.to_datetime(df['data_pedido'], format='mixed', errors='coerce') # Convertendo Data de STR pra Date e ordenando

#Correção Valores Nulos
df['cliente_id'] = df['cliente_id'].fillna('CLI-N/I')
df['email'] = df['email'].fillna('Email não informado')
df['avaliacao'] = df['avaliacao'].fillna(0)

#Correção nos dados
df['nome_cliente'] = df['nome_cliente'].str.title()
df['estado'] = (
    df['estado']
    .str.upper()
    .str.replace(r'^S.*', 'SP', regex=True)
    .str.replace('RIO', 'RJ', regex=True)
)

print(df.dtypes)
print(df.tail(20))
