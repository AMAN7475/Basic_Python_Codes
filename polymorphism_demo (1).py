def area(x,y=None):
	if y == None : 
		return (22/7)*x*x
	else : 
		return (x*y)

"""def area(x):
	return 3.14*x*x

def area(x,y) : 
	return x*y"""


r = int(input("Enter Radius : "))
l,b = int(input("Enter Length : ")),int(input("Enter Breadth : "))
area_of_circle = area(r)
area_of_rectangle = area(l,b)

print("Area of Circle : ",area_of_circle)
print("Area of Rectangle : ",area_of_rectangle)