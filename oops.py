class Parent:
    a=0
    b=0
    def __init__(self,x,y):
        self.a=x
        self.b=y
        print("Calling parent class constructor")

    def Add(self):
        c=self.a+self.b
        print("Add=",c)

class Child(Parent):
    p=0
    b=0
    def __init__(self,l,m):
        self.p=l
        self.b=m
        super().__init__(l,m)
        print("Calling Child class constructor")
    def Sub(self):
        c=self.p-self.b
        print("Sub=",c)



c1=Child(90,20)
c1.Add()
c1.Sub()