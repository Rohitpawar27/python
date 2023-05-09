e=int(input("enter english marks"))
m=int(input("enter maths marks"))
s=int(input("enter science marks"))
total=e+m+s
per=total/3
print("total",total)
print("per",per)
grade=""
if(per<40):
    grade="poor"
elif(per>=40 and per<=59):
    grade="average"
elif(per>=60 and per<=80):
    grade="good"
else:
    grade="excellent"

print("total",total)
print("per",per)
print("grade",grade)