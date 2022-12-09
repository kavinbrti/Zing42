import mysql.connector as sql



myDb = sql.connect(host="localhost",user="root",passwd="Kavin@2000",database="zing",auth_plugin='mysql_native_password')

myCursor = myDb.cursor()
q = "select * from COMDATA"
myCursor.execute(q)
zing = myCursor.fetchall()
if(myDb):
    print("connection successful")
else:
    print("Failed")
