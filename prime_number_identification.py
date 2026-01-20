n = int(input("Enter Number :"))
for i in range (2,n):
	if n % i == 0:
 		print ("Composite")
 		break
else:
 	print ("Prime")


#Prime No Checking by While Loop#
x = int(input("Enter No : "))
i = 2

while i < x:
    if x % i == 0:
        print("{} is composite".format(x))
        break
    i += 1      
else:
    print("{} is prime".format(x))
        