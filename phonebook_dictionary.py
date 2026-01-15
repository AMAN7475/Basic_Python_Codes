Master_Data_Dictionary = [{"Name":"Aman","Contact":"123456789","Email":"aman@gmail.com"},{"Name":"Raj","Contact":"4444444444444","Email":"raj@gmail.com"},{"Name":"Shubham","Contact":"77777777777","Email":"shubham@gmail.com"}]

def create_contact():
	name = input("Enter Name : ")
	contact = input("Enter Contact Number : ")
	email = input("Enter Email Address :")

	contact_entry = {"Name":name,"Contact":contact,"Email":email}
	Master_Data_Dictionary.append(contact_entry)
	print(Master_Data_Dictionary)
	file_1 = open("Master_Data_Dictionary","w")
	file_1.write("contact_entry")
	file_1.close()
	print(Master_Data_Dictionary)
	return

def display_contact():
	for i in Master_Data_Dictionary:
		print("Name : ", i["Name"])
		print("Contact : ", i["Contact"])
		print("Email : ", i["Email"])
		print()
	return
	

def search_contact():
	search = input("Enter name to search : ")

	for i in Master_Data_Dictionary:
		if i["Name"].lower() == search.lower():
			print("Name : ", i["Name"])
			print("Contact : ", i["Contact"])
			print("Email : ", i["Email"])
			return
	else:
		print("Contact not found.")	
		return search_contact()	

def update_contact():
	update = input("Enter the contact name to be updated : ")

	for i in Master_Data_Dictionary:
		if i["Name"].lower() == update.lower():
			print("Contact Found.Enter New Details")
			i["Name"] = input("Enter New Name : ")
			i["Contact"] = input("Enter New Contact : ")
			i["Email"] = input("Enter New Email : ")
			print("Contact updated successfully")
			print(Master_Data_Dictionary)
			return
	else:
		print("Contact not found.")
		return update_contact()

def delete_contact():
	delete = input("Enter contact name to be deleted : ")

	for i in Master_Data_Dictionary:
		if i["Name"].lower() == delete.lower():
			Master_Data_Dictionary.remove(i)
			print("Contact deleted successfully")
			print(Master_Data_Dictionary)
			return 				
	else:
		print("Contact not found.")
		return delete_contact()

def choice_selection(value):
	choice = int(input("Press 1 to Add Contact\nPress 2 to Display All Contacts\nPress 3 to Search Contact\nPress 4 to Update Contact\nPress 5 to Delete Contact\nPlease enter a valid choice : "))

	if choice == 1:
		create_contact()

	elif choice == 2:
		display_contact()	

	elif choice == 3:
		search_contact()

	elif choice == 4:
		update_contact()

	elif choice == 5:
		delete_contact()

	else:
		print("Invalid Input.Please select a valid input")		
		return choice_selection(value)


print("Welcome to Aman's Phonebook")

Phonebook = choice_selection(Master_Data_Dictionary)

