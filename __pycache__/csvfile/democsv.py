import pandas as pd 
# data=pd.read_csv("student.csv")
# print(data)
data={"employee_id":[1,2,3,4,5],"salary":[10000,20000,30000,40000,15000]}
df=pd.DataFrame(data)
print(df)
df.to_excel("employees.xlsx")