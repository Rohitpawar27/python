# class Myclass:
#     def Addition(self):
#         print("called default Add function")

#     def Addition (self,a):
#         print("called Add function with int parameter")

#     def Addition(self,a,b):
#         print("called Add function with two parameter")

#     def Addition (self,a,b,c):
#         print("called Add function three parameter")

# m=Myclass()
# m.Addition(90,80,70)
# m.Addition(90,80)
# m.Addition(80,90,60)
# m.Addition()


class Abc:
    def Add(self,a,b):
        c=a+b
        print("Add",c)

class Xyz(Abc):
    def sub (self,a,b):
        c=a-b
        print("sub",c)

x1=Xyz()
x1.Add(80,70)
x1.sub(90,80)

