m=int(input("Enter your Mark:"))
if(m>=50):
    if m>91 and m<=100:
        print("Your Grade is A1")
    if m>81 and m<91:
        print("Your Grade is A2")
    if m>71 and m<81:
        print("Your Grade is B1")
    if m>61 and m<71:
        print("Your Grade is B2")
    if m>51 and m<61:
        print("Your Grade is C1")
    if m>41 and m<51:
        print("Your Grade is C2")
    if m>31 and m<41:
        print("Your Grade is D")
    if m>21 and m<31:
        print("Your Grade is E1")
    if m>0 and m<21:
        print("Your Grade is E2")
else:
    print("You are Fail")
