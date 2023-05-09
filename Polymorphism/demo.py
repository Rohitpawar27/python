# Functions polymorphism

class BEStudent:
    def Details(self):
        print("BE Student Details called")
    def Profile(self):
        print("BE Student Profile called")

class BCAStudent:
    def Details(self):
        print("BCA Student Details called")
    def Profile(self):
        print("BCA Student Profile called")

def call (abc):
    abc.Details()
    abc.Profile()

be=BEStudent()
bca=BCAStudent()
call (be)
call (bca)
