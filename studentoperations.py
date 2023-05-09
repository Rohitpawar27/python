class Operations:
    studentdata=[]
    def AddStudent(self):
        rno=int(input("enter roll no"))
        name=input("Enter Name")
        eng=int(input("Enter English marks"))
        math=int(input("Enter Maths marks"))
        sci=int(input("Enter science marks"))
        st={"rno":rno,"name":name,"english":eng,"maths":math,"science":sci}
        self.studentdata.append(st)
    def DisplayAlltStudents(self):
        for d in self.studentdata:
            print(str(d["rno"])+" "+str(d["name"])+" "+str(d["english"])+" "+str(d["maths"])+" "+str(d["science"]))
    def GetStudentByRno(self):
        x=int(input("enter number"))
        for d in self.studentdata:
            if d["rno"]==x:
                print(str(d["name"])+" "+str(d["english"])+" "+str(d["maths"])+" "+str(d["science"]))

    def UpdateStudent(self):
        rno=int(input("enter roll no"))
        name=input("Enter Name")
        eng=int(input("Enter English marks"))
        math=int(input("Enter Maths marks"))
        sci=int(input("Enter science marks"))
        st={"rno":rno,"name":name,"english":eng,"maths":math,"science":sci}
        index=-1
        for d in self.studentdata:
            # print(d)
            if(d["rno"]==rno):
                index=self.studentdata.index(d)
                break 
        self.studentdata[index]=st
        print("Updated Successfully")
    def Deletestudent(self):
        x=int(input("enter number"))
        for d in self.studentdata:
         if d["rno"]==x:   
          self.studentdata.remove(str(d["rno"]))
    def calculatepercentage(self):
        for d in self.studentdata:
            total=(d["english"]+d["maths"]+d["science"])
            d=(total/300)*100
            print(d,"%")
            print("total percentage")
    def grades(self):
        for d in self.studentdata:
            total=(d["english"]+d["maths"]+d["science"])
            d=(total/300)*100
            print(d,"%")
        if (d<35):
            print("you are fail")
        elif(d>35 and d<60):
            print("your marks are average")
        elif(d>60 and d<80):
            print("your marks are good")
        elif (d>80 and d<100):
            print("your marks are excellent")
            print(d,"grades")
    def passedorfailed (self):
        for s in self.studentdata:
            total=(s["english"]+s["maths"]+s["science"])
            d=(total/300)*100
            if (d>35):
                print(str(s["rno"])+" "+str(s["name"])+" "+str(s))
            else:
                print("you are fail")
            


