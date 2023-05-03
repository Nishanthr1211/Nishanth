#............Two numbers to add,sub,mul,div,mod.................#
while(1):
    x=str(input("Do You Want To Continue Yes/No:"))
    if(x=='Yes'):
        m=int(input("Enter First number:"))
        n=int(input("Enter Second number:"))
        c=m+n
        print(c)
        if(c==7):
            print("The Sub:",m-n)
            print("The Mul:",m*n)
            print("The Mod:",m/n)
            print("The rem:",m%n)
    else:
        break;
    
        
