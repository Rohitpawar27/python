f=open("squares.txt","r")
data=f.read()
cnt=0
for d in data:
    if (d=="1"):
        cnt+=1
print ("total count of 1="+str(cnt))