var_1 = ["25", 2.5, 25, 25+4j,25]
print(var_1)
print (type(var_1))

for i in range (len(var_1)):
	print(var_1[i])
	print(type(var_1[i]))

for j in var_1:
	print (j)
	print(type(j))	

var_1.append("Mohit")
print(var_1)	

var_1.insert(3,"Indore")
print(var_1)

x = var_1.index("Indore")
var_1[x]="Bhopal"
print(var_1)

x = var_1.pop()
print(x)
print(var_1)

x = var_1.remove("25")
print(var_1)

del(var_1)

