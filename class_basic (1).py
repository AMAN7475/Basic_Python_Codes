class contact:
	def __init__(self):
		self.name = input("Enter Name : ")
		self.email = input("Enter Email : ")
		self.phone = input("Enter Phone : ")

	def show(self):
		print("============================")
		print("Contact Name : ",self.name)
		print("Contact Email : ",self.email)
		print("Contact Phone : ",self.phone)
		print("============================")

	def update(self):
		choice = input("Press 1 to Change Name\nPress 2 to Change Email\nPress 3 to Change Phone No.\nEnter a valid Choice : ")
		if choice == "1":
			self.name = input("Enter New Name : ")
		elif choice == "2":
			self.email = input("Enter New Email : ")
		elif choice == "3":
			self.phone = input("Enter New Phone : ")
		else : 
			print("Invalid Choice")

	def delete(self):
		choice = input("Press 1 to Delete Name\nPress 2 to Delete Email\nPress 3 to Delete Phone No.\nEnter a valid Choice : ")
		if choice == "1":
			self.name = ""
		elif choice == "2":
			self.email = ""
		elif choice == "3":
			self.phone = ""
		else : 
			print("Invalid Choice")



"""c1 = contact()
#print(type(c1))

c1.show()
c1.update()
c1.show()"""


c1 = contact()

while True:
    print("--- Menu ---")
    print("1. Add New Contact")
    print("2. Show All Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

choice = input("Enter your choice (1-6): ")

if choice == "1":
    c = contact()
    phonebook.append(c)
    print("Contact added successfully.")

elif choice == "2":
    if not phonebook:
        print("No contacts to show.")
    else:
        for i, contact in enumerate(phonebook):
            #print(f"\nContact #{i + 1}")
            contact.show()

elif choice == "3":
    name_to_search = input("Enter name to search: ").lower()
    found = False
    for contact in phonebook:
        if contact.name.lower() == name_to_search:
            contact.show()
            found = True
            break
    if not found:
        print("Contact not found.")

elif choice == "4":
    name_to_update = input("Enter name to update: ").lower()
    found = False
    for contact in phonebook:
        if contact.name.lower() == name_to_update:
            contact.update()
            print("Contact updated.")
            found = True
            break
    if not found:
        print("Contact not found.")

elif choice == "5":
    name_to_delete = input("Enter name to delete: ").lower()
    found = False
    for contact in phonebook:
        if contact.name.lower() == name_to_delete:
            phonebook.remove(contact)
            print("Contact deleted.")
            found = True
            break
    if not found:
        print("Contact not found.")

elif choice == "6":
    print("Exiting Phonebook. Goodbye!")
    	break

else:
    print("Invalid choice. Please try again.")