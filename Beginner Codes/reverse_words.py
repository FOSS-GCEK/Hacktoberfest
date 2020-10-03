string=input("Enter string:")
string_list=string.split()
reverse_list=[]
rev_str=""
length=len(string_list)
for i in range(-1,-(length+1),-1):
    reverse_list.append(string_list[i])
reverse=rev_str.join(reverse_list)
print(reverse)
