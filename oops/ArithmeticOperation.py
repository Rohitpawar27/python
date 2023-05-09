class Operation:
    a=0
    b=0
    def __init__(self,x,y):
           self.a=x
           self.b=y
    def Addition(self):
        c=self.a+self.b
        print("Addition",c)
    def Substraction (self):
        c=self.a-self.b
        print("Substraction",c)
    def Multiplication (self):
        c=self.a*self.b
        print ("multiplication",c)
    def Division(self):
        c=self.a/self.b
        print("Division",c)

