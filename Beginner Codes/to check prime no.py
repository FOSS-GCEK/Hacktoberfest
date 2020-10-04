#logic - by using a additional variable and checking condition on it

num = int(input("Enter a number."))
n = 0
for i in range(2,num):
	if(num % i == 0):
		n = n + 1
		print("its not prime no.")
		break	
if(n == 0):
	print("its a prime no.")
	
celsius = int(input("Enter temp."))

fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
