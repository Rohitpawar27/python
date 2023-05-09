class Teacher:
    tid=""
    tname=""
    def setdata(self,a,b):
        self.tid=a
        self.tname=b
    def getdata(self):
        print(self.tid)
        print(self.tname)


    
class Student(Teacher):
    rollno=""
    sname=""
    def putdata(self,x,y):
        self.rollno=x
        self.sname=y
    def printdata(self):
        print(self.rollno)
        print(self.sname)



s=Student()
s.putdata(1,"Urmila")
s.printdata()
s.setdata(2,"Rushika")
s.getdata()


    
