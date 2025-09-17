#write a py script to crud of employee and manager in an organization 
class employee : 
	def __init__(self):
		self.id = int(input("Enter Id : "))
		self.ename = input("Enter Employee Name : ")
		self.eemail = input("Enter Employee Email : ")
		self.econtact = input("Enter Employee Contact : ")

	def emp_show(self):
		print("Employee Id : ",self.id)
		print("Employee Name : ",self.ename)
		print("Employee Email : ",self.eemail)
		print("Employee Contact : ",self.econtact)

	def emp_update(self):
		con_choice = True
		choice = input("Press 1 to change Name\nPress 2 to change Email\nPress 3 to change Contact\nPlease Enter a valid choice : ")
		while con_choice == True :
			if choice == "1" :
				self.ename = input("Enter New Name : ")
				break
			elif choice == "2" :
				self.eemail = input("Enter New Email : ")
				break
			elif choice == "3" :
				self.econtact = input("Enter New Contact : ")
				break
			else :
				print("Invalid Choice")
				con_choice	= True
		else : 
			print("Employee data updated successfully")
			con_choice	= False

E1 = employee()
E1.emp_show()
E1.emp_update()
E1.emp_show() 