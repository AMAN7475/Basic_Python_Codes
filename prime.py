n = int(input("Enter Value : "))
for i in range (2,n):
	if n%i == 0 : 
		print ("{} is composite".format(n))
		break
else :
	print ("{} is prime".format(n))

		
