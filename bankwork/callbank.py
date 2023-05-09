from datainput import customer
b=customer()
i=1
while(i!=0):
    ch=int(input("enter choice\n1.addcustomer\n2.login"))
    if(ch==1):
       b.addcustomer()
    elif(ch==2):
        b.login()

    i=int(input("do you want continue?yes(1)/no(0)")) 