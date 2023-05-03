while(1):
    x=str(input("Are You Continue Yes or No:"))
    if(x=='yes'):
        print(x)
        a=str(input("Enter the first string name:"))
        b=str(input("Enter the Second string name:"))
        m=a.split()
        n=b.split()
        for d in m:
            if d in n:
                print(d)
    else:
        break;
