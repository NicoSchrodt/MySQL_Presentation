import mysql.connector

def create_connection(host, user, password, database):
    mydb = mysql.connector.connect(
      host=host,
      user=user,
      password=password,
      database=database
    )
    return mydb

def execute_statement(mydb, statement):
    mycursor = mydb.cursor()
    mycursor.execute(statement)
    myresult = mycursor.fetchall()
    return myresult

'''
mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="rootpsw1",
      database="database1"
    )
    
    #print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM new_table")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
'''