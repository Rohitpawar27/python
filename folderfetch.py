import os
# data=os.listdir("D:\\Telegram")
# print(data)
# for d in data:
#     print(d)
# data=os.listdir("D:\\Telegram\\Peaky Blinders S1 to S5")
# print (data)
# for d in data:
#     print(d)

data=os.listdir("D:\\Telegram\\Peaky Blinders S1 to S5")
cnt=0
for d in data:
    if "p" in d:
        cnt=cnt+1
        print (d)
print (str(cnt))
