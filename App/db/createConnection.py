import mysql.connector


def createConnection(DB_DADOS, databaseName=""):
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host=DB_DADOS['host'],
            user=DB_DADOS['user'],
            password=DB_DADOS['password'],
            database=databaseName
        )
    finally:
        return mydb
