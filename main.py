import database

connection = database.create_connection("localhost", "root", "rootpsw1", "dhbw_base")

result = database.execute_statement(connection, "SELECT * FROM students")

for x in result:
    print(x)