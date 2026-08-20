import mysql.connector
mydb = mysql.connector.connect(host="localhost",user = "root", passwd = "radheshyam@57", database = "kodnest")
mycursor = mydb.cursor()

mycursor.execute("show databases")
for i in mycursor:
    print(i)

mycursor.execute("show databases")

for i in mycursor:
    print(i)


"""import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="student"
)

mycursor = mydb.cursor(buffered=True)

mycursor.execute("SHOW TABLES")

for table in mycursor.fetchall():
    print(table)"""