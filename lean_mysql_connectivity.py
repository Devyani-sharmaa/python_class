# !pip install mysql-connector-python

import mysql.connector

coon = mysql.connector.connect(host = "localhost", username = "root", password = "devyani@12", database = "excellence")

# if coon.is_connected():
#     print("database connected sucessfully")


curser = coon.cursor()

# curser.execute('insert into Students values("pria", 98347598, "lkfn@gmail.com");')
# curser.execute('delee from.....')

#curser.execute('insert into Students values("devyani",12345,"brd1234@gmail.com");')


curser.execute("select * from Students;")

#coon.commit()

zx = curser.fetchall()

print(zx)     