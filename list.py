list1=['Nishanth','R','KCG']
list2=['KCG','COLLEGE','TRAINEE']
list3=[]
for d in list1:
    for m in list2:
        if m==d:
            list3.append(m)
print(list3)
