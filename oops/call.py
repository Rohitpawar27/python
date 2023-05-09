import AritmeticOperations as op

i=1
while(i!=0):
    ch=int(input("Enter Your Choce\n1.Add\n2.Sub\n3.Mul\n4.Div"))
    if(ch==1):
        op.Addition()
    elif(ch==2):
        op.Substraction()
    elif(ch==3):
        op.Multiplication()
    elif(ch==4):
        op.Division()
    else:
        print("Please Enter corerct choice")
    i=int(input("Do You wants to continue?Yes(1)/No(0)"))
    