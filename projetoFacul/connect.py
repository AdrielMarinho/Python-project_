import MySQLdb
from tkinter import messagebox


def db_connect():
    try:
        conn = MySQLdb.connect(
            db='fakesteam',
            host='nfdb.mysql.database.azure.com',
            user='nfadministrator',
            passwd='nftrabalho#231D',
            ssl=False
        )
        return conn
    except MySQLdb.Error:
        messagebox.showinfo("Erro", "Erro ao se conectar no banco de dados")
        exit()


def db_desconnect(conn):
    if conn:
        conn.close()
