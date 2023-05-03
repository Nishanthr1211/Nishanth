s_name=[]
students=[]

def student():
    name=input(" Enter the name : ")
    reg_no=input(" Enter the reg_no : ")
    student={}
    student["name"]=name  
    student["reg_no"]=reg_no  
    students.append(student)

def Student(name):
    flag=False
    result=0
    for n in students:
        if(n["name"]==name):
            flag=True
            result =n["reg_no"]
    return result
a=1
while(a):
    print("type 1 for reg student")
    print("type 2 for search student")
    print("type 3 for student list")
    res=int(input())
    #n=3
    #for i in range(0,n):
       # student()
    #print(students)
   # name=input("enter student name search: ")
    #s=Student(name)
    
    if(res==1):
        student()
        continue
    elif(res==2):
        if(len(students)):
            name=input("enter student name search: ")
            s=Student(name)
            if(s): 
                print("student found & reg.no is: ",s)
            else:
                print("student not found ")
        else:
            print("empty student list")
        
    elif(res==3):
        if(len(students)):
            print(students)
        else:
            print("empty student list")
    else:
        print("Invalid value")
        continue
    
    print("are you want to continue? press 1 for yes, 0 for no")
    a=int(input(""))
