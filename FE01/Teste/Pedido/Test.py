# -*- coding: utf-8 -*-

import mysql.connector
from datetime import date, datetime, timedelta

cnx = mysql.connector.connect(user='python', password='Python1!',
                              host='127.0.0.1',
                              database='pedidos')

print("PedidosApp")


def registarpedido():
    print("Numero de Paciente:")
    paciente = int(input())
    query = ("SELECT * FROM Doente "
             "WHERE idDoente = " + str(paciente))
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    if result is None:
        print("Doente not found")
        quit(1)
    print("Doente Identifiado:" + str(result[2]))
    print("Episodio")
    episodio = int(input())
    print("Observacoes:")
    orbservacoes = input()
    hoje = datetime.now().date()
    inserir = ("INSERT INTO Pedido "
               "(idPedido, Estado, data, Observacoes, Doente_idDoente, idEpisodio, Relatorio)"
               "VALUES (NULL, %(estado)s, %(data)s, %(obser)s,%(doente)s,%(episodio)s,%(relatorio)s)")
    data = {
        'data': hoje,
        'estado': "Scheduled",
        'obser': orbservacoes,
        'doente': paciente,
        'episodio': episodio,
        'relatorio': ""
    }
    cursor.execute(inserir, data)
    cnx.commit()
    cursor.close()
    print ("Registo Concluído")


def alterarpedido():
    print("Numero de Paciente:")
    paciente = int(input())
    query = ("SELECT * FROM Doente "
             "WHERE idDoente = " + str(paciente))
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    if result is None:
        print("Doente not found")
        quit(1)
    print("Doente Identificado:" + str(result[2]) + "\n")
    print("Pedidos atuais do doente:")
    getInfo = ("SELECT idPedido, Observacoes FROM pedido AS P"
               "    INNER JOIN doente AS D ON D.idDoente = P.Doente_idDoente"
               "    WHERE idDoente = " + str(paciente) + " AND Estado = 'Scheduled'"
                                                         "    OR Estado = 'Changed'")
    cursor.execute(getInfo)
    for row in cursor:
        getId, getObs = str(row).split(",")
        lixo, idPedido = getId.split("(")
        lixo, obs, lixo = getObs.split('\'')
        print("Pedido nº: " + idPedido + "   Observações: " + obs + "\n")

    idPedido = input("Pedido que deseja alterar:")
    obs = input("Altere as observações:")
    alteraPedidoQuery = ("UPDATE pedido SET Observacoes = '" + str(obs) +
                         "', Estado='Changed' WHERE idPedido=" + str(idPedido) + ";")
    cursor.execute(alteraPedidoQuery)
    cnx.commit()
    cursor.close()
    print("Alteração efetuada com sucesso")


while True:
    print("1 - Registar Pedido")
    print("2 - Alterar Pedido")
    res = int(input())
    if res == 1:
        registarpedido()
    if res == 2:
        alterarpedido()
    else:
        print("Erro!")
