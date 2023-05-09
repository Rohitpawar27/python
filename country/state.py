import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="countries")
mycursor=con.cursor()
sname=input("enter state name")
i=1
cities=[]
while (i!=0):
    cname=input("enter city name")
    cities.append(cname)
    i=int(input("wants to add more cities?yes(1)/no(0)"))
st={"state_name":sname, "cities":cities}
print (st)
mycursor.execute("insert into states(state_name) values ('"+sname+"')")
con.commit()
mycursor.execute("select max(state_id)state_id from states")
data=mycursor.fetchall()
print (data)
sid=data[0][0]
for c in cities:
    mycursor.execute("insert into cities(city_name,state_id)values ('"+c+"',"+str(sid)+")")
    con.commit()
    


print("finished")
