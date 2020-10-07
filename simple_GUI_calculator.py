
from tkinter import *

operator = "" 


def press(num): 
	global operator 
	operator = operator + str(num) 
	equation.set(operator) 


 
def equalpress(): 
	try: 
		global operator  
		total = str(eval(operator)) 
		equation.set(total) 
		operator = "" 
	except: 
		equation.set(" error ") 
		operator = "" 


def clearpress(): 
	global operator 
	operator = "" 
	equation.set("") 

 
if __name__ == "__main__": 
	root = Tk()  
	root.title("My calculator") 
	root.geometry("356x125") 
	equation = StringVar() 

	operator_field = Entry(root, textvariable=equation) 
	operator_field.grid(columnspan=4, ipadx=70) 


	button1 = Button(root, text=' 1 ', fg='black', bg='white', command=lambda: press(1), height=1, width=7) 
	button1.grid(row=2, column=0) 

	button2 = Button(root, text=' 2 ', fg='black', bg='white', command=lambda: press(2), height=1, width=7) 
	button2.grid(row=2, column=1) 

	button3 = Button(root, text=' 3 ', fg='black', bg='white', command=lambda: press(3), height=1, width=7) 
	button3.grid(row=2, column=2) 

	button4 = Button(root, text=' 4 ', fg='black', bg='white', command=lambda: press(4), height=1, width=7) 
	button4.grid(row=3, column=0) 

	button5 = Button(root, text=' 5 ', fg='black', bg='white', command=lambda: press(5), height=1, width=7) 
	button5.grid(row=3, column=1) 

	button6 = Button(root, text=' 6 ', fg='black', bg='white', command=lambda: press(6), height=1, width=7) 
	button6.grid(row=3, column=2) 

	button7 = Button(root, text=' 7 ', fg='black', bg='white', command=lambda: press(7), height=1, width=7) 
	button7.grid(row=4, column=0) 

	button8 = Button(root, text=' 8 ', fg='black', bg='white', command=lambda: press(8), height=1, width=7) 
	button8.grid(row=4, column=1) 

	button9 = Button(root, text=' 9 ', fg='black', bg='white', command=lambda: press(9), height=1, width=7) 
	button9.grid(row=4, column=2) 

	button0 = Button(root, text=' 0 ', fg='black', bg='white', command=lambda: press(0), height=1, width=7) 
	button0.grid(row=5, column=0) 

	plus = Button(root, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=1, width=7) 
	plus.grid(row=2, column=3) 

	minus = Button(root, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=1, width=7) 
	minus.grid(row=3, column=3) 

	multiply = Button(root, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=1, width=7) 
	multiply.grid(row=4, column=3) 

	divide = Button(root, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=1, width=7) 
	divide.grid(row=5, column=3) 

	equal = Button(root, text=' = ', fg='black', bg='white', command=equalpress, height=1, width=7) 
	equal.grid(row=5, column=2) 

	clearpress = Button(root, text='clear', fg='black', bg='white', command=clearpress, height=1, width=7) 
	clearpress.grid(row=5, column='1') 

	root.mainloop() 