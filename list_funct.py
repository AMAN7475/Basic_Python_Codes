#Write py script to demonstrate crud operation of List 
#List = Heterogenious, Duplicate values are allowed, Indexed, ordered and Mutable 


#create a list 
list_x = ["Sunny","Raikwar","Raikwar",12.5,35,"M"]
print(list_x)
print(type(list_x))


# reading the list element one by one 
for i in range(len(list_x)):
	print(list_x[i])
	print(type(list_x[i]))

# Iteratable Method 
for j in list_x :
	print(j)

#Update a list 
#add a element 
#adding element at last 
list_x.append("Indore")

print(list_x)
#adding element at specific Location 
list_x.insert(1,"Raikwar")
print(list_x)

#updating or Changing an element 
y = list_x.index("Raikwar")
list_x[y] = "Sharma"
print(list_x)

#deleting 
list_x.pop()
print(list_x)

list_x.remove("Raikwar")
print(list_x)

#deleting the entire list 
del(list_x)

print(list_x)


