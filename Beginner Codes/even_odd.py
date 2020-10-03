num = int(input("Enter a number: "))
f=1
if(num==0):
    print("Factorial is zero")
else:
    for i in range(1,num+1):
        f=f*i
    print("Factorial is {0}".format(f))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
