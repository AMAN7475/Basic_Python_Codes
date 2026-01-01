def duplicate_remove(x):
	y = []
	for i in (x):
		if i not in y:
			y.append(i)
	return(y)



A = [1,1,2,2,2,3,4,5,6,7,8,8]
B = []

for i in (A):
	B =	duplicate_remove(A)

print(B)

