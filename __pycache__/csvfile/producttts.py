import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
st={"product":["pen","pencil","compass","notebook","pen","pencil","compass","notebook","pen","pencil","compass","notebook"],"year":[2010,2011,2012,2013,2010,2011,2012,2013,2010,2011,2012,2013],"profit":[10000,12000,9000,15000,8000,9000,13000,16000,7000,8500,10500,20000]}
df=pd.DataFrame(st)
# print(df)
data=df.groupby(["product","year","profit"])
print(data.get_group("year"))
data=df.groupby("year")
print(data)
for group,d in data:
    print(group)
    print(d)
for group,dt in data:
    print(group)
    print(data)
# product_profit=df.groupby("product")['profit'].sum()

# print(product_profit)
# yearly_product_profit=df.groupby(['year','product'])['profit'].sum()
# print(yearly_product_profit)
# df.pd.Dataframe(st)
# df.plot(kind='bar',x='year' ,y='profit' ,color='red')
# plt.title('Bar plot')
# plt.show()
# pencil_df=df[df["product"]=="pencil"]

# plt.plot(pencil_df["year"],pencil_df["profit"])
# df.plot(kind='Bar',x='year',y='profit',color='red')
# plt.show()

product=input("enter roduct name")
pencil_df=df[df["product"]==(product)]
plt.plot(product['year'],product['profit'])
df.plot()
ply.show()

