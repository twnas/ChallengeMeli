from db.checkIfDatabaseExists import checkIfDatabaseExists


def createDatabase(sqlConnection, databaseName):
    exitCode = 0
    if sqlConnection.is_connected():
        if checkIfDatabaseExists(sqlConnection, databaseName) == 0:
            try:
                mycursor = sqlConnection.cursor()
                mycursor.execute("CREATE DATABASE "+databaseName)
                exitCode = 1
                print("La base de datos: '"+databaseName +
                      "' fue creada")

            except:
                exitCode = -1
            finally:
                return exitCode
