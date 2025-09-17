x = "4*3/2-4+2"
result = []
num = ""

for i in x:
	if i.isnumeric():
		num = num + i 

	else:
		result.append(int(num))	
		result.append(i)

print(result)		