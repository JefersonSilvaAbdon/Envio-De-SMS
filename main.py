#Você vai precisar do Pandas - pip install pandas
#Você vai precisar do Twilio - pip install twilio

import pandas as pd
from twilio.rest import Client
# Pegar seu SSID no site twilio.com/console
account_sid = "seu ssid"
# Pegar seu token no site twilio.com/console
auth_token  = "seu token"
client = Client(account_sid, auth_token)

# Abrir o arquivo excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Verificar algum valor na coluna vendas daquele arquivo
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # Se for maior do que 55000 -> Envia um SMS com o NOme, o mês e as vendas do vendedor
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+5571-seunumeroparareceber-",
            from_="+numerodotwilio",
            body=f'No mês de {mes}, {vendedor} bateu a meta com R${vendas} reais')
        print(message.sid)

# Caso não seja maior do que 55.000 não quero fazer nada