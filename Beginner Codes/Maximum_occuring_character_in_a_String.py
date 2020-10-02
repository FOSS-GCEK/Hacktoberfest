_Simple python program to find the maximum occuring character in a string._

s=input("Please enter a String")
d={}
c={}
for i in s:
    if i in c:
        c[i]+= 1
    else:
        c[i]=1
    d.update({i:c[i]})
occ=max(d.values())
s= max(d,key = d.get)
print(s,occ)
