import pandas as pd 

students={"rno":[1,2,3,4,5,6],"names":["rohit","akash","hemant","shrikant","onkar","shripad"]}
studentsubjects={"rno":[1,3,5,7,9,4],"subjects":["english","maths","science","marathi","hindi","python"]}
left=pd.DataFrame(students)
right=pd.DataFrame(studentsubjects)
# print(left)
# print(right)
# data=pd.merge(left, right,on="rno")
# data=pd.merge(left, right,on="rno",how="right")
# data=pd.merge(left, right,on="rno",how="left")
data=pd.merge(left, right,on="rno",how="outer")

print(data)