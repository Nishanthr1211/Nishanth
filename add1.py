#............find the Dictionary..............#
a={"nishanth":329,"naresh":224,"BCA":229}
b=a.keys()
for d in b:
    if 'n' in d:
        print("n is Present")
    else:
        print("n is not present")
    

a={"number":20,"number1":40,"number2":60}
b=a.values()
total=0
total=sum(b)
print("Dictionary is:",total)



    
#..........function............#

def sub(a,b):
    c=a-b
    return c
while(1):
    d=str(input("Continue Yes/No:"))
    if(d=='yes'):
        a=int(input("enter the number:"))
        b=int(input("enter another number:"))
        sub(a,b)
        c=sub(a,b)
        print(c)
        if(c==0):
            print("Valid")
        else:
            print("Not Valid")
    else:
        break;
    
#.............Call by value...........#
def name(*x):
    print("my name is:"+x[3])
    print("my name is:"+x[0])
name("Hari","Ranjith","Sabarish","Nishanth")


def name2(**x):
    print("my name is:"+x["name1"])
name2(name="Hari",name1="Nishanth")


'''
 
