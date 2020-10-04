str="Hello Hai"
t=set({})
for i in str:
    c=0
    for j in str:
        if(i==j):
            c+=1
    if(c>1):
        t.add(i)