giventextsentences="Nishanth"
sentence="R.Nishanth"
sentence+="Nishanth.R"

word=sentence.split()
words=sorted(word)
d={}
for w in word:
    if w in d:
        d[w]+=1
    else:
        d[w]=1
    for x in d.keys():
        print(x,"\t",d[x])
