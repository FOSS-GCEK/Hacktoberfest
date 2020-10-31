#METHOD -1 ( WITH THIRD VARIABLE)..
#take inputs from user.
x =int(input("enter the first number = ") 
y =int(input("enter the second number = ") 
#now take the new variable , do following squence.
temp = x
x = y
y = temp
#print the result after swapping and its sum.
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
print('The sum of x and y: {}'.format(x+y))
#end of file.
       
#METHOD-2(WITHOUT THIRD VARIABLE ).
#take inputs from user.
x =int(input("enter the first number = ") 
y =int(input("enter the second number = ") 
x = x + y  
y = x - y  
x = x - y  
print("After Swapping: x =", x, " y =", y); 
#end of code.
