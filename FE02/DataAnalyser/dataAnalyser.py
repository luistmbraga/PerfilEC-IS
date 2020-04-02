import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
con = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='fe02MaquinaA')

query = "SELECT mensagemTxt, roundTripTime FROM fe02maquinaa.mensagem order by LENGTH(mensagemTxt) ASC, roundTripTime ASC "
cursor = con.cursor(buffered=True)
cursor.execute(query)

msgTam = []
roundTime = []

for (mensagemTxt, roundTripTime) in cursor:

    msgTam.append(len(mensagemTxt))
    roundTime.append(roundTripTime)

cursor.close()

df=pd.DataFrame({'x': msgTam, 'y': roundTime })

plt.plot( 'x', 'y', data=df, marker='o', color='skyblue')
plt.title("Round Trip Time em função do tamanho", loc='left', fontsize=12, fontweight=0, color='black')
plt.xlabel("Tamanho")
plt.ylabel("Round Trip Time (s)")
plt.show()


query = "SELECT numMensagens, tempoGeracao FROM fe02maquinaa.batch order by numMensagens ASC"
cursor = con.cursor(buffered=True)
cursor.execute(query)

numM = []
tGeracao = []

for (numMensagens, tempoGeracao) in cursor:

    numM.append(numMensagens)
    tGeracao.append(tempoGeracao)

cursor.close()


df2=pd.DataFrame({'x': numM, 'y': tGeracao })

plt.plot( 'x', 'y', data=df2, marker='o', color='skyblue')
plt.title("Tempo de Geração em função do número de Mensagens", loc='left', fontsize=12, fontweight=0, color='black')
plt.xlabel("número de mensagens")
plt.ylabel("tempo de geração (s)")
plt.show()