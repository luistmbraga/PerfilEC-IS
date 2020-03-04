# -*- coding: utf-8 -*-

import mysql.connector
from datetime import date, datetime, timedelta


cnx = mysql.connector.connect(user='python', password='Python1!',
                              host='127.0.0.1',
                              database='exames')

print("ExamesApp")


def realizarExame():
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
    query2 = ("SELECT * FROM Pedido "
              "where Doente_idDoente = " + str(paciente))
    cursor.execute(query2)
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        print("Nenhum Exame Encontrado")
    pedidos = []
    for element in result:
        print("Pedido:{} \n"
              "Data:{:%d de %b de %Y} \n"
              "Observações:{} \n".format(element[0], element[2], element[3]))
        pedidos.append(element[0])
    while True:
        print("Escolha o Pedido")
        res = int(input())
        if res in pedidos:
            break
        else:
            print("Pedido Errado!")
    print("Relatório:")
    report = input()
    update = ("UPDATE Pedido "
              "SET Relatorio= %(relatorio)s, Estado='Complete'"
              "WHERE idPedido=%(pedido)s")
    data = {
        'pedido': res,
        'relatorio': report

    }
    cursor.execute(update, data)
    cnx.commit()
    cursor.close()
    print ("Test Concluído")


while True:
    print("1 - Realizar Exame")
    res = int(input())
    if res == 1:
        realizarExame()
    if res == 2:
        pass
