import mysql.connector

try:
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    cursor1 = dataBase.cursor()
    cursor1.execute("CREATE DATABASE StudentDatabase")
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database=dataBase,
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


    def buttonClick():
        a = e1.get()
        print(a)

    screen1 = tk.Tk()
    screen1.title('Score Filter')
    l1 = tk.Label(screen1, text="Enter the minimum grade to filter:")
    l1.pack()
    e1 = tk.Entry(screen1)
    e1.pack()
    b1 = tk.Button(text="ENTER", width=10, bg="white", fg="red", font="Arial 20 bold", command=buttonClick)
    b1.pack()
    screen1.mainloop()

except mysql.connector.Error as error:
    print("Database error")
