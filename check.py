'''
while(1):
    x=str(input("Are you continue Yes/No:"))
    if(x=='yes'):
        a={'1:10','2:20','3:30','4:40','5:50','6:60'}
        b=(input("Enter the numbers:"))
        if b in a:
            print("Available")
        else:
            print("Not Available")
    else:
        break;

a={'1:10','2:20','3:30','4:40','5:50','6:60'}

print(dict[::-1])


#..........Reverse..............#
a={'1:10','2:20','3:30','4:40','5:50','6:60'}
for x in a:
    m=a[::-1]
    print("Reverse Sorted dictionary is :")
    print(m)
'''
#.........Sorted.......#
a = {'c': 3, 'a': 1, 'd': 4,'b': 2}
b = sorted([(x, y) for (y,x) in a.items()])
print("Sorted dictionary is :")
print(b)
c=b[::-1]
print("Reverse Sorted dictionary is :")
print(c)

