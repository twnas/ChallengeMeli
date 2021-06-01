from db.checkIfTableExists import checkIfTableExists


def createTable(sqlConnection, databaseName, tableName, columns):
    exitCode = 0
    if sqlConnection.is_connected():
        if checkIfTableExists(sqlConnection, databaseName, tableName) == 0:
            try:
                mycursor = sqlConnection.cursor()

                mycursor.execute("CREATE TABLE `"+databaseName +
                                 "`.`"+tableName+"` "+columns)
                exitCode = 1
                print("La tabla: '"+tableName +
                      "' fue creada")

            except:
                exitCode = -1
            finally:
                return exitCode


