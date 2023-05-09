import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="collegedb")
mycursor=con.cursor()
mycursor.execute("DELETE from students where rno=3")
con.commit()
print ("Deleted Successfully")