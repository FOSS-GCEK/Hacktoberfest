#
# multiple addition and subtraktion
# 
def multiAddAndSub(calculation):
	if type(calculation) == str:
		values = []
		values = calculation.split("+")
		result = 0
		# first check, if there are numbers i can subtract
		for i in range(len(values)):
			values[i] = values[i].replace(" ", "")
			if "-" in set(values[i]):
				values2 = values[i].split("-")
				values[i] = values2[0]
				values2.pop(0)
				for n in range(len(values2)):
					values[i] = str(int(values[i]) - int(values2[n]))
			result += int(values[i]) # then i add the values
	return result

print("Please enter only integer.")
print(multiAddAndSub(input("=")))
