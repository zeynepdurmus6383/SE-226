import mysql.connector
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
cursor1 = dataBase.cursor()
createQuery = "CREATE TABLE IF NOT EXISTS StudentDatabase"
cursor1.execute(createQuery)
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="StudentDatabase",
    password="root"
)
if (connection.is_connected()):
    cursor2 = connection.cursor()
    tableQuery = "CREATE TABLE IF NOT EXISTS Students(" \
                 "ID INT NOT NULL AUTO_INCREMENT, " \
                 "Name VARCHAR(30), " \
                 "SCORE INT, " \
                 "PRIMARY KEY(ID))"
    cursor2.execute(tableQuery)
    while (true):
        sName = input("Enter student name or -1 to quit:")
        if (sName == "-1"):
            break
        sScore = input("Enter student score:")
        insertQuery = "INSERT INTO Students(Name,Score) " \
                      "VALUES(%s,%s)"
        insertValues = (sName, sScore)
        cursor2.execute(insertQuery, insertValues)
