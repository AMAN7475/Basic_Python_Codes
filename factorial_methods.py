
#Iterative Method  
def Iterative_Method(x):
	fact = 1 
	for i in range(1,x+1):
		fact *= i

	return fact


#Recursion Method
def Recursion_Method(x):
	if x == 0 or x == 1:
		return 1

	else:
		return x * Recursion_Method(x-1)

