import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="collegedb")
mycursor=con.cursor()
mycursor.execute("select * from students")
data=mycursor.fetchall()
# print(data)
for d in data:
    print(str(d[0])+" "+d[1]+" "+str(d[2])+" "+str(d[3])+" "+str(d[4]))