import mysql.connector

mydb = mysql.connector.connect(host="localhost",user='root',password='Siddharth@1#',database='myfirstdb')

mycursor = mydb.cursor()
mycursor.execute("select * from student")

# result = mycursor.fetchall()
result = mycursor.fetchone()
for i in result:
    print(i)