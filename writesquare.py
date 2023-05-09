f=open("squares.txt","w")
i=1
for i in range(1,101):
    f.write("square of+str+(i)"+" = "+str(i*i)+"\n")
f.close()
print("finished")