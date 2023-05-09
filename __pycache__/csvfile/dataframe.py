import pandas as pd 
st={"employee_id":[1,2,3,4,5],"Names":["Rohit","Hemant","Akash","Shrikant","Onkar"],"Designation":["Accountant","manager","Sales_Head","HR","Sales_Head"],"salary":[10000,20000,30000,40000,15000]}
df=pd.DataFrame(st)
# print(df)
data=df.groupby ("Designation")
# print(da)
# print(data.get_group("Sales_Head")
for group,dt in data:
 print(group)
 print(dt)
