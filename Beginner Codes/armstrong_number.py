#storing the input of int datatype given by user in a variable.
num = int(input("Enter a number: "))
#taking another variable and alotting the value.
sum = 0
#now, again storing the same input value in temp variable.
temp = num
#loop starts.
while temp > 0:
#below squences of 3 lines are segregating digits and adding it.
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
#chacking the final value from loop is equal to input value or not.
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
   #end of code.
