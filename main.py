#Você vai precisar do Pandas
#Você vai precisar do smtplib
#Você vai precisar do pip install openpyxl

import smtplib
from email.message import EmailMessage
import pandas as pd
import win32com.client as client

# Dados E-mail
#Email = 'apitestar40@gmail.com'
#Email_senha = 'unijorge2022'

# Abrir o arquivo excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Verificar algum valor na coluna vendas daquele arquivo
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # Se for maior do que 55000 -> Envia um SMS com o NOme, o mês e as vendas do vendedor
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        outlook = client.Dispatch('Outlook.Application')
        message = outlook.CreateItem(0)
        message.Display()
        message.To = "201001737@unijorge.com.br"
        message.Subject = "ALGUÉM BATEU A META"
        message.Body = (f'No mês de {mes}, {vendedor} bateu a meta com R${vendas} reais')
        message.Save()
        message.Send()
        #Criar email
        #msg = EmailMessage()
        #msg['Subject'] = 'ALGUEM BATEU A META'
        #msg['From'] = "apitestar40@gmail.com"
        #msg['To'] = "201001737@unijorge.com.br"
        #msg.set_content(f'No mês de {mes}, {vendedor} bateu a meta com R${vendas} reais')

#Enviar o e-mail
#with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#   smtp.login(Email, Email_senha)
#    smtp.send_message(msg)

#        print(message.sid)

# Caso não seja maior do que 55.000 não quero fazer nada