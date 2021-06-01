from db.checkIfTableExists import checkIfTableExists


# INSERT INTO `databases_classification` (`uid`, `db_name`, `owner_email`, `manager_email`, `integrity`, `availability`, `confidentiality`) VALUES('aaaaaaaaaa', 'bbbbbbbbbbb', 'cccccccccccc', 'ddddddddddddddddddd', 'eeeeeeeeeeeeeeeeee', 'ffffffffffffffff', 'ggggggggggggggg')


def insertData(sqlConnection, databaseName, tableName, data):
    print(data)
    exitCode = 0
    if sqlConnection.is_connected():
        if checkIfTableExists(sqlConnection, databaseName, tableName) == 1:
            try:
                sqlConnection.database = databaseName
                mycursor = sqlConnection.cursor()
                sql = ("INSERT INTO `"+tableName +
                       "` (`uid`, `db_name`, `owner_email`, `manager_email`, `integrity`, `availability`, `confidentiality`) VALUES (%s, %s, %s, %s, %s, %s,%s)")
                sqlConnection.commit()

                mycursor.execute(sql, data)
                exitCode = 1
                print("La linea fue agregada a la base de datos")
            except:
                print("Erro")
                exitCode = -1
            finally:
                return exitCode
