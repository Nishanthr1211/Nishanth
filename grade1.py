m=int(input("ENTER YOUR MARK"))
if((m>=50)and(m<=100)):
    if(m<=90):
        if(m<=80):
            if(m<=70):
                if(m<=60):
                    print("Grade is D")
            else:
                print("Grade is C")
        else:
            print("Grade is B")
    else:
        print("Grade is A")
else:
    print("You are Failed")
    
