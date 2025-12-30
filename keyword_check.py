from keyword import iskeyword

x = input("Enter your string : ")
y = iskeyword(x)

if y == True:
	print ("Given string is a keyword")

else:
	print("Given string is not a keyword")	