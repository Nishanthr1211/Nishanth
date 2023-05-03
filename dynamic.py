s_name=[]
students=[]

def Student():
    name=input("Enter the Name:")
    Reg_no=input("Enter the Reg_no:")
    student={"name":name,"Reg_no":Reg_no}
    students.append(student)
        
def student(student):
    flag=False
    result=0
    for n in students:
        if (n["name"]==student):
            flag=True
            result=n["Reg_no"]
    return result
n=2
for i in range(0,n):
    Student()
s=input("Enter the name to search:")
result=student(s)
if(result):
    
    print("Student Found & Reg.No is:",result)
else:
    print("Student Not Found")
