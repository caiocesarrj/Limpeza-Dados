import pandas as pd
import numpy as np


df = pd.read_csv(r'C:\Projetos\Limpeza-Dados\DadosBrutos\pedidos_raw.csv')

df = df.drop_duplicates(subset='id_pedido', keep='first') # Remove duplicatas

#Correção e Remoção de Valores Nulos
df['cliente_id'] = df['cliente_id'].fillna('CLI-N/I')
df['avaliacao'] = df['avaliacao'].fillna(0)
df = df.dropna(subset=['quantidade', 'preco_unitario']) #Removendo quantidades e precos nulos, não tem valor de receita


#Conversões
df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce').astype('Int64') # Quantidade de Float para Int
df['data_pedido'] = pd.to_datetime(df['data_pedido'], format='mixed', errors='coerce') # Convertendo Data de STR pra Date e ordenando


#Correção nos dados
df['nome_cliente'] = df['nome_cliente'].str.title() # Padronizando nomes
df['estado'] = (
    df['estado']
    .str.upper()
    .str.replace(r'^S.*', 'SP', regex=True)
    .str.replace('RIO', 'RJ', regex=True)
)                                            #Padronizando Estados
df['status'] = df['status'].str.upper()

df.loc[df['desconto'] > 1, 'desconto'] = np.nan # Descontos acima de 100% retornam desconhecido

df['preco_unitario'] = df['preco_unitario'].abs() # Valores negativos para positivos


#Receita de pedidos entregues, devolvidos e cancelados
df_valido = df[df['status'] == 'ENTREGUE'] #Para calculo de receita
df_cancelado = df[df['status'] == 'CANCELADO']
df_devolvido = df[df['status'] == 'DEVOLVIDO']



print(df.head(10))

df.to_csv(r'C:\Projetos\Limpeza-Dados\Pedidos_Limpos.csv', index = False, encoding='utf-8')
df_check = pd.read_csv(r'C:\Projetos\Limpeza-Dados\Pedidos_Limpos.csv')
print('Df salvo com sucesso')
