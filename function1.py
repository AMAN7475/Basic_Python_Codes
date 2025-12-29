#Write a py script calculate permutation of r over n value
#Write a py script calculate Combination of r over n value 

#permutation = n! / (n-r)!
#Combination = n!/ r! * (n-r)!

'''n = int(input("Enter N value : "))
r = int(input("Enter R value : "))

fact_n = 1
for i in range(1,n+1):
	fact_n = fact_n * i 

fact_nr = 1
for j in range(1,n-r+1):
	fact_nr = fact_nr * j 

npr = fact_n / fact_nr
print("Permutation of {} over {} = {}".format(r,n,npr))'''


def fact(x):
	result = 1
	for i in range(1,x+1):
		result = result * i
	return result

n = int(input("Enter N value : "))
r = int(input("Enter R value : "))

fact_n = fact(n)

fact_nr = fact(n-r)

fact_r = fact(r)

ncr = fact_n / (fact_r * fact_nr)
print("Combination of {} over {} = {}".format(r,n,ncr))



