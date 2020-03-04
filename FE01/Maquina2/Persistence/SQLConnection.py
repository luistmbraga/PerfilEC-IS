import mysql.connector

class SQLConnection:
    def __init__(self):
        self.con = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='maquina2')

    def get_con(self):
        return self.con
