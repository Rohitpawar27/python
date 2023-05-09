class student :
    rno=""
    name=" "
    def setdata(self,r,n):
        self.rno=r
        self.name=n
    def getdata(self):
        print (self.rno)
        print (self.name)
s=student()
s.setdata(10,"rohit")
s.getdata()