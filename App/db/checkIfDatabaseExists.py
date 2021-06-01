def checkIfDatabaseExists(sqlConnection, databaseName):
    if sqlConnection.is_connected():
        mycursor = sqlConnection.cursor()
        exitCode = 0
        try:
            mycursor.execute("SHOW DATABASES")
            for x in mycursor:
                if databaseName.lower() == x[0]:
                    exitCode = 1
        except:
            exitCode = -1
        finally:
            return exitCode
