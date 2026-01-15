n = int(input("Enter value of n:"))
r = int(input("Enter value of r :"))

fact_n = 1
for i in range(1,n+1) :
	fact_n = fact_n * i

fact_nr = 1
for j in  range(1,n-r+1):
	fact_nr = fact_nr * j

	Permutation = fact_n/ fact_nr

	print("Permutation of {} over {} = {}". format(r,n,Permutation))


#PERMUTATION USING WHILE LOOP#
"""n = int(input("Enter value of n : "))
r = int(input("Enter value of r : "))

fact_n = 1
i = 1 
while i <= n:
    fact_n = fact_n * i
    i +=1 
    
fact_nr = 1
j = 1 
while j <= r:
    fact_nr = fact_nr * j
    j +=1 

Permutation = fact_n/fact_nr

print("Permutation of {} over {} = {}".format(n,r,Permutation))"""
