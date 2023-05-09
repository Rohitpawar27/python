import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="collegedb")
mycursor=con.cursor()
mycursor.execute("UPDATE students SET name='Hema',english=35,maths=45,science=55 where rno=3")
con.commit()
print ("successfully updated")