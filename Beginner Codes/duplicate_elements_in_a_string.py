string=input("Enter a string:")
set_dupli=set({})
for i in string:
    count=0
    for j in string:
        if(i==j):
            count+=1
    if(count>1):
        set_dupli.add(i)
print("Duplicate elements are: {}".format(set_dupli))

