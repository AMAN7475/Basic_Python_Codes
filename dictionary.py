dict_x = {"Name":"Aman","Age":"27","City":"Indore"}
print(dict_x)
print(type(dict_x))

#Only Key
for i in dict_x:
	#print(i)
	print(dict_x[i])

#Only Value	
for j in dict_x.values():
	print(j)

#Both key and value
for i,j in dict_x.items():
	print(i)
	print(j)

#Adding a key value
dict_x["contact"] = "123345566"
print(dict_x)

#Change in dictionary
dict_x["Name"] = "Raj"
print(dict_x)

#Delete
dict_x.pop("Age")
print(dict_x)