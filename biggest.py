#......To call the value after which is biggest number to find...........#
data=[]
n=int(input("Enter the Size"))
for x in range(n):
    data.append(int(input("enter the value")))
print(data)
a=data[0]
for d in data:
     if(d>a):
      a=d
print(a)
