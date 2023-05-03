s_name=[]
def Student():
    name=input("Enter the Name:")
    s_name.append(name)
def student(name):
    flag=False
    for n in name:
        if (n==s_name):
            flag=True
    return flag
n=5
for i in range(0,n):
    Student()
s=student("Nishanth")
if(s):
    print("Student Found")
else:
    print("Student Not Found")
