import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data={"product_name":["pen","pencil","compass","notebook","pen","pencil","compass","notebook","pen","pencil","compass","notebook"],
      "years":[2010,2010,2010,2010,2011,2011,2011,2011,2012,2012,2012,2012],
      "profit":[10000,12000,9000,15000,8000,9000,13000,16000,7000,8500,10500,20000]}
df=pd.DataFrame(data)
new=df.groupby(["product_name"])

for groupa, d in new:
    a=np.array(groupa)
    b=np.array(d)
    print(b)
    print(a)
    
pro=df.groupby("years")
for groupb,i in pro:
    print(groupb)
    print(i)
    y=np.array(groupb)
    x=np.array(i)
    
    print("year wise",x)
    
    pro=df.groupby("profit")
    for groupc,x in pro:
        print(groupc)
        print(x)
        h=np.array(x)
        
        
    product=input("enter product name")
    product_g=df[df['product_name']==(product)]
    plt.plot(product_g['years'],product_g['profit'])
    df.plot()
    plt.show()