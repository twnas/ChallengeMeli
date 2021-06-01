from Configs import DADOS_EMAIL, DADOS_DB
from db.createConnection import createConnection
from db.createDatabase import createDatabase
from db.createTable import createTable
from db.insertData import insertData

from mail.message import createMessage
from mail.send import sendEmail

import sys
import csv
import json

mySqlConnection = createConnection(DADOS_DB)
if mySqlConnection == None:
    print("Por favor verifique las informaciones de la base de Datos")
    sys.exit()

dbName = "meli_challenge"
createDatabase(mySqlConnection, dbName)

columns = "(uid VARCHAR(255), db_name VARCHAR(255), owner_email VARCHAR(255), manager_email VARCHAR(255), integrity VARCHAR(255), availability VARCHAR(255), confidentiality VARCHAR(255))"
tableName = 'databases_classification'
createTable(mySqlConnection, dbName, tableName, columns)

lista_usuarios = []
with open("userList.csv", encoding='utf-8') as users_refer:
    users = csv.reader(users_refer, delimiter=',')
    for linha in users:
        id = linha[0]
        user = linha[1]
        state = linha[2]
        manager_mail = linha[3]
        lista_usuarios.append(
            {"id": linha[0], "user": linha[1], "state": linha[2], "manager_mail": linha[3]})


def clearDbClassification():
    return {"dn_name": None, "confidentiality": None,
            "integrity": None, "availability": None, "uid": None, "owner_email": None, "manager_email": None}


def getManagerEmail(userList, uid):
    for usuario in userList:
        if usuario['user'] == uid:
            return usuario['manager_mail']


db_classification = clearDbClassification()


def getDataAsTuple(db_classification):
    return (db_classification["uid"], db_classification["dn_name"], db_classification["owner_email"], db_classification["manager_email"], db_classification["integrity"], db_classification["availability"], db_classification["confidentiality"])

with open('dblist.json') as json_file:
    data = json.load(json_file)
    for p in data["db_list"]:
        try:
            db_classification["dn_name"] = p["dn_name"]
            db_classification["confidentiality"] = p["classification"]["confidentiality"]
            db_classification["integrity"] = p["classification"]["integrity"]
            db_classification["availability"] = p["classification"]["availability"]
            db_classification["uid"] = p["owner"]["uid"]
            db_classification["manager_email"] = getManagerEmail(
                lista_usuarios, db_classification["uid"])
            db_classification["owner_email"] = p["owner"]["email"]
        except:
            pass
        finally:
            print("Guardando en la Base de Datos")
            insertData(mySqlConnection, dbName, tableName,
                       getDataAsTuple(db_classification))
            if db_classification["confidentiality"] == "high":
                print("Enviando email")
                email = createMessage("Seguridad Informatica", db_classification["manager_email"], "Alta Seguridad", "Informacion de Alta Seguridad")
                sendEmail(DADOS_EMAIL, email)
            elif db_classification["integrity"] == "high":
                print("Enviando email")
                email = createMessage("Seguridad Informatica", db_classification["manager_email"], "Alta Seguridad", "Informacion de Alta Seguridad")
                sendEmail(DADOS_EMAIL, email)
            elif db_classification["availability"] == "high":
                print("Enviando email")
                email = createMessage("Seguridad Informatica", db_classification["manager_email"], "Alta Seguridad",
                                      "Informacion de Alta Seguridad")
                sendEmail(DADOS_EMAIL, email)