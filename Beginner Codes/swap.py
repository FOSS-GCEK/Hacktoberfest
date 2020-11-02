#METHOD-1 USING THIRD VARIABLE.
x = int(("Enter the number1 = "))
y = int(input("Enetr the number2 = "))
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
print('The sum of x and y: {}'.format(x+y))

#METHOD-2 WITHOUT USING THIRD VARIABLE.
x = int(input("Enter the number1 = "))
y = int(input("Enetr the number2 = "))
x = x + y 
y = x - y
x = x - y
print('The value of number1 after swapping: {}'.format(x))
print('The value of number2 after swapping: {}'.format(y))
#END OF CODE.
