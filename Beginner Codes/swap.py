x = 5
y = 10

temp = x
x = y
y = temp


print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
print('The sum of x and y: {}'.format(x+y))

#another approach for swap without temrarory variable
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
print("Before UpdateA :{0} B:{1}".format(a,b))
a=a+b
b=a-b
a=a-b
print("After update A :{0} B:{1}".format(a,b))
