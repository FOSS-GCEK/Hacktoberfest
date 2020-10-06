a=int(input("enter the number"))
sum1=0
while a>0:
	rem=a%10
	sum1+=rem
	a=a//10
sum1+=a
print("sum is=",sum1)

