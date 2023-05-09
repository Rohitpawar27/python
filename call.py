from studentoperations import Operations
op=Operations()
i=1
while(i!=0):
    ch=int(input("Enter Choice\n1.Add Student\n2.Display All Students\n3.Get Student By Rno\n4.Update Student\n5.Delete student\n6.calculatepercentage\n7.grades\n8.passedorfailed"))
    if(ch==1):
        op.AddStudent()
    elif(ch==2):
        op.DisplayAlltStudents()
    elif(ch==3):
        op.GetStudentByRno()
    elif(ch==4):
        op.UpdateStudent()
    elif(ch==5):
        op.Deletestudent()
    elif(ch==6):
        op.calculatepercentage()
    elif(ch==7):
        op.grades()
    elif(ch==8):
        op.passedorfailed()
    i=int(input("Do you wants to Conitiue?Yes(1)/No(0)"))
    
