# prime number
# data=[1,3,7,11,31,41,91,23,29]

# for d in data:
#     cnt=0
#     for i in range(2,d):
#         if(d%i==0):
#             cnt=cnt+1
#     if (cnt==0):
#         print(d)

# palindrome number

# d = [101,102,212,333,123,313]
# x=d
# sum=0
# while (d!=0):
#      rem=d%10
#      sum=rem+sum*10
#      n=math.floor(d/10)
#      if (sum==x):
#       print (d)

# data=[1,2,3,4,5,6,7,8,9]
# max = data[0]
# for d in data:
#     if (d>max):
#         max=d
# print ("max="+str(max))

# data=[1,2,3,4,5,6,7,8,9]
# min = data[0]
# for d in data:
#     if (d<min):
#         min=d
# print ("min="+str(min))

data=[88,6,1,4,3,7,99,5]
print (data.sort())
print (data)
print ("secon largest element=",sorted(data)[-2])





         


