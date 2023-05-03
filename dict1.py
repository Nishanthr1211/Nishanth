
a={"brand":"Enfiled","Model":"Classic","Year":1964}
print(a)

#.......update.........#
'''
a.update({"color":"white","class":"first hand"})
print(a)
'''
#......for loop......#
'''
a=str(input("Enter the name:"))
b=int(input("Enter the age:"))
for x in a:
    if x in b:
print(x)
'''
#..........For Loops..........#

for x in a:
    print(x)

for x in a:
    print(a[x])

for x in a.values():
    print(x)


for x in a.keys():
    print(x)


print("only keys from dict keys")
for x in a.keys():
    print(x)

for x,y in a.items():
    print(x,y)
al=a.items()
print(al)

for x in al:
    print(x)











print(al)
