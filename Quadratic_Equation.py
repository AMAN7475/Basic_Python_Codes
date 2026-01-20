import math
def equation_roots (a ,b ,c ):

	# Calculate discriminant using formula.

	discriminant = ((b**2) - (4*a*c))

	if discriminant > 0:
		print("Roots are Real and Different.")
		print((-b )+ math.sqrt(discriminant) / (2*a))
		print((-b )- math.sqrt(discriminant) / (2*a))

	elif discriminant == 0:
		print ("Roots are Real and Same")
		print((-b )+ math.sqrt(discriminant) / (2*a))
		print((-b )- math.sqrt(discriminant) / (2*a))

	else:
		print("Roots are Complex") 
       
a = int(input(" Enter a : "))
b = int(input(" Enter b : "))
c = int(input(" Enter c : "))

if a == 0:
	print("Invalid Input")
else:	
	equation_roots(a,b,c)		