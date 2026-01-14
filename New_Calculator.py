# Function to add two numbers
def add(num_A,num_B):
	return (num_A + num_B)

# Function to substract two numbers
def substract(num_A,num_B):
	return (num_A - num_B)

# Function to multiply two numbers
def multiply (num_A,num_B):
    return (num_A * num_B)	

# Function to divide two numbers
def divide (num_A,num_B):
   return (num_A / num_B)

# Function to convert float value into integer value 
def convert_to_int(value):
	if value.is_integer():
		return int(value)
	else:
		return value	  

#Function to identify the input type
def identify_input(value):

	if value.isnumeric():
		return int(value)

	elif value.replace(".","").isnumeric():
		return float(value)	

	else:
		return str(value)		


num_A = input("Enter 1st value: ")
num_B = input("Enter 2nd value: ")

num_A = identify_input(num_A)
num_B = identify_input(num_B)

next_2 = True
while next_2:

	if isinstance(num_A, int) == True and isinstance(num_B, int) == True:
		Select = input("Press 1 : for Addition\nPress 2 : for Substraction\nPress 3 : for Multiplication\nPress 4 : for Divison :\nSelect a valid Operation : ")	
		
		if Select == "1" :
			print(num_A, "+", num_B, "=",add(num_A,num_B))
			
		elif Select == "2":
			print(num_A, "-", num_B, "=",substract(num_A,num_B))
			
		elif Select == "3":
			print(num_A, "*", num_B, "=",multiply(num_A,num_B))
			
		elif Select == "4":
			print(num_A, "/", num_B, "=",divide(num_A,num_B))
			
		else :
			print ("Invalid Input")	

		next_calculation = input("Let's do next calculation? (Y/N): ")
		if next_calculation == "N":
			next_2 = False		


	elif isinstance(num_A, int) == True and isinstance(num_B, float) == True:
		Select = input("Press 1 : for Addition\nPress 2 : for Substraction\nPress 3 : for Multiplication\nPress 4 : for Divison :\nSelect a valid Operation : ")	
		
		if Select == "1" :
			(num_A, "+", num_B, "=",add(num_A,num_B))
			print (convert_to_int(add(num_A,num_B)))
			
		elif Select == "2":
			(num_A, "-", num_B, "=",substract(num_A,num_B))
			print (convert_to_int(substract(num_A,num_B)))

		elif Select == "3":
			(num_A, "*", num_B, "=",multiply(num_A,num_B))
			print (convert_to_int(multiply(num_A,num_B)))

		elif Select == "4":
			(num_A, "/", num_B, "=",divide(num_A,num_B))
			print (convert_to_int(divide(num_A,num_B)))
		
		else:
			print("Invalid Input")	


		next_calculation = input("Let's do next calculation? (Y/N): ")
		if next_calculation == "N":
			next_2 = False	
			

	elif isinstance(num_A, float) == True and isinstance(num_B, int) == True:
	
		Select = input("Press 1 : for Addition\nPress 2 : for Substraction\nPress 3 : for Multiplication\nPress 4 : for Division\nSelect a valid Operation : ")
		
		if Select == "1" :
			(num_A, "+", num_B, "=",add(num_A,num_B))
			print (convert_to_int(add(num_A,num_B)))
			
		elif Select == "2":
			(num_A, "-", num_B, "=",substract(num_A,num_B))
			print (convert_to_int(substract(num_A,num_B)))

		elif Select == "3":
			(num_A, "*", num_B, "=",multiply(num_A,num_B))
			print (convert_to_int(multiply(num_A,num_B)))

		elif Select == "4":
			(num_A, "/", num_B, "=",divide(num_A,num_B))
			print (convert_to_int(divide(num_A,num_B)))

		else :
			print ("Invalid Input")	
			

		next_calculation = input("Let's do next calculation? (Y/N): ")
		if next_calculation == "N":
			next_2 = False	


	elif isinstance(num_A, float) == True and isinstance(num_B, float) == True:
	
		Select = input("Press 1 : for Addition\nPress 2 : for Substraction\nPress 3 : for Multiplication\nPress 4 : for Division\nSelect a valid Operation : ")
		
		if Select == "1" :
			(num_A, "+", num_B, "=",add(num_A,num_B))
			print (convert_to_int(add(num_A,num_B)))
			
		elif Select == "2":
			(num_A, "-", num_B, "=",substract(num_A,num_B))
			print (convert_to_int(substract(num_A,num_B)))

		elif Select == "3":
			(num_A, "*", num_B, "=",multiply(num_A,num_B))
			print (convert_to_int(multiply(num_A,num_B)))

		elif Select == "4":
			(num_A, "/", num_B, "=",divide(num_A,num_B))
			print (convert_to_int(divide(num_A,num_B)))

		else :
			print ("Invalid Input")	
			

		next_calculation = input("Let's do next calculation? (Y/N): ")
		if next_calculation == "N":
			next_2 = False			
			

	elif isinstance(num_A, str) == True and isinstance(num_B, str) == True:
		
		Select = input("Press 1 : for Addition\nPress 2 : for Multiplication\nSelect a valid Operation : ")

		if Select == "1":
			print(num_A+num_B)

		elif Select == "2":
			print("Re-input Values")

			num_A = input("Enter 1st value: ")
			num_B = input("Enter 2nd value: ")

			num_A = identify_input(num_A)
			num_B = identify_input(num_B)

		next_calculation = input("Let's do next calculation? (Y/N): ")
		if next_calculation == "N":
			next_2 = False		


	elif isinstance(num_A, str)	== True and isinstance(num_B, int) == True:

		Select = input("Press 1 : for Multiplication ")

		if Select == "2":
			print("num_A"*"num_B")

		else:
			print("Invalid Input")	

		next_calculation = input("Let's do next calculation? (Y/N): ")
		if next_calculation == "N":
			next_2 = False		