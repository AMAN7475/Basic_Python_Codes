def circle_circumference(x):
	PI = 3.14
	circumference = 2*PI*x

	return circumference

n = int(input("Enter no. of Iteration :"))
for j in range (n):
	r = int(input("Enter radius :"))
	c = circle_circumference(r)
	print ("Circumference of circle with radius {} = {}".format(r,c))