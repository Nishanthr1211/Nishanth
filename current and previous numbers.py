#...........7.Question..........#
a=int(input("Enter a number:"))
factorial=1
if a<0:
    print("Factorial does not exist for negative number")
elif a==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,a+1):
        factorial=factorial*i
        print("The factorial of",a,"is",factorial)


#..........6.Question...........#
a=int(input("Enter the table:"))
for i in range(0,11):
    print(a,"x",i,"=",a*i)



#.........5.Question...........#
n=[0,1,2,3,0]
if(n[0]==n[-1]):
    print("True")
else:
    print("False")


#.......4.Question.........#
a=[1,2,3,4,5,6,1]
if(a[0]==a[-1]):
    print("Matched")
else:
    print("Does not match")

#...........3.Question..............#
a=0
for x in range(a,10):
    sum1=a+x
    print("Current",x,"Previous number",a,"sum:",a+x)
    a=x


#.............2.Question.............#
a={"name":"nishanth","class":"BCA","class":"BCA","reg.no":329}
b=list(dict.values(a))
print(b)


#...............1.Question............#
list=[]
x=int(input("Enter the total values:"))
for i in range(x):
    a=int(input("Enter the Values:"))
    list.append(a)
    print(min(list))
    print(max(list))
