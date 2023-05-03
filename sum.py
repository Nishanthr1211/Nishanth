al=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
word="boat"
total=len(word)
sum=0
result=0
ans=[]
for x in range(0,len(word),1):
    sum=al.index(word[x])+1
    result=result+sum
    ans.append(sum)
    if(x==len(word)-1):
       print(result)
for y in range(0,len(word),1):
    print(ans[y])
