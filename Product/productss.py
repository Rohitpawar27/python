import pandas as pd
import mysql.connector

df=pd.read_csv("products.csv")
st=df["name"]
pr=df["price"]
sc=df["stock"]
# print(len(st))
con=mysql.connector.connect(host="localhost",user="root",password="",database="production")
mycursor=con.cursor()
for i in range (0,len(st)):
    insert= "INSERT INTO pr (product_name,product_price,stock) VALUES ('"+st[i]+"',"+str(pr[i])+","+str(sc[i])+")"
# values=data.VALUES.tolist()
    mycursor.execute(insert)
con.commit()
print("successfully")