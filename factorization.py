num = int(input("Enter Value : "))
x = num
factor = []
prime = []
factor_repeat = []

for i in range(2,num):
	if x%i == 0 :
		factor.append(i)
print("Factor : ",factor)

for j in factor : 
	for k in range(2,j):
		if j % k == 0 :
			break 
	else : 
		prime.append(j)
print("Prime Factor : ",prime)


for m in prime :
	while x > 0 :
		if x % m == 0 : 
			factor_repeat.append(m)
		x = x // m 

		

print(factor_repeat)

