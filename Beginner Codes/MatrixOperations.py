import numpy as np

x = np.array([[1, 2], [4, 5]]) 
y = np.array([[7, 8], [9, 10]])

print(x)
print(y)

print('Addition of numbers :')
print(np.add(x,y))



print('Sub of numbers :')
print(np.subtract(x,y))


      
print('Mul of numbers :')
print(np.multiply(x,y))


      
print('Div of numbers :')
print(np.divide(x,y))



print('Sqrt of numbers :')
print(np.sqrt(x))


print ("The product of matrices is : ") 
print (np.dot(x,y))


#Transpose
print ("Transpose of matrix x is : ") 
print (x.T)

print ("Transpose of matrix y is : ") 
print (y.T)
