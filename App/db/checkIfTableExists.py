def checkIfTableExists(sqlConnection, databaseName, tableName):
    if sqlConnection.is_connected():
        mycursor = sqlConnection.cursor()
        exitCode = 0
        try:
            mycursor.execute("USE "+databaseName)
            mycursor.execute("SHOW TABLES")
            for x in mycursor:
                if tableName.lower() == x[0]:
                    exitCode = 1
        except:
            exitCode = -1
        finally:
            return exitCode
