'''
while(1):
    x=str(input("Are you sure to continue Yes/No:"))
    if(x=='yes'):
        a={"name":"Nisahnth","class":"BCA"}
        b={"name":"Nishanth","class":"BCA"}
        c=input("Enter the object:")
        if c in a:
            if c in b:
                print(a[c],b[c])
    else:
        break;

#.........Dictionary........#
a={"name":{"Nisahanth","BCA"},"College":"IslamiahCollege"}
b={"address":"Vaniyambadi"}
x={"name":"Nisahanth", "College":"IslamiahCollege" ,"address":"Vaniyambadi"}
i=input("Enter the value:")
print('\n')
print(x)

#.............List............#
a=["name",["Nisahanth","BCA"],"College","IslamiahCollege"]
b={"address":"Vaniyambadi"}
x={"name",{"Nisahanth","College":"IslamiahCollege"},"address":"Vaniyambadi"}
i=input("Enter the value:")
print('\n')
print(x)
'''
#..........Two String add dictionary..............# 
a="name" '\t'"reg.no" '\t'"college"
b="Nishanth"'\t' "329"'\t' "KCG"
c=a.split()
d=b.split()
c1={}
for x in range(len(c)):
    c1[c[x]]=d[x]
    print(c1)

