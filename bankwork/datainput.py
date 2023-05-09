import mysql.connector

class customer :
    def addcustomer (self):
        n=input("enter customer name")
        a=int(input("enter account number"))
        m=input("enter mobile number")
        ma=input("enter mail id")
        at=input("enter account type")
        ab=input("enter account balance")
        pw=str(input("enter password"))
        con=mysql.connector.connect(host="localhost",user="root",password="",database="bank")
        mycursor=con.cursor()
        mycursor.execute("insert into customer(customer_name,account_number,mobile_number,email,acc_type,acc_balance,password) values('"+n+"',"+str(a)+",'"+str(m)+"','"+str(ma)+"','"+str(at)+"',"+str(ab)+",'"+pw+"')")
        con.commit()
        print("Successfully Inserted")

        
    def login (self):
        a=int(input("enter account number"))
        p=input("enter password")
        con=mysql.connector.connect(host="localhost",user="root",password="",database="bank")
        mycursor=con.cursor()
        mycursor.execute("select * from customer  where account_number="+str(a)+ " and password='"+p+"'")
        data=mycursor.fetchall()
        if(len(data)>0):
            print("Login Success")
        else:
            print("Login Failed")