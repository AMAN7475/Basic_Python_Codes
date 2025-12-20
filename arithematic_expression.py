#exp = "23+12-7-3*234/14+4"
#exp = ["23","+","12","-","7","-","3","*","234","/","14","+","4"]


# expression = operators and operands

#Precedence and Associativity

#25/5
#2<5

#step 1 : Convert string expression to operator and Operand
#step 2 : Check Validity of Expression
#step 3 : Convert Infix to Prefix or Postfix
#step 4 : Solve the Prefix or Postfix expression form

opr = {"/":1, "*":1, "+":2, "-" : 2}

#step 1 : Convert string expression to operator and Operand
def expression() : 
	user_exp = input("Enter Arithematic Expression : ")
	exp = []
	item = ""
	for i in user_exp : 
		if i not in opr : 
			item = item + i
		else : 
			if item != "" : 
				exp.append(item)
			exp.append(i)
			item = ""
	else : 
		if item != "" : 
			exp.append(item)


	print("User  Expression : ",user_exp)
	print("Converted Expression : ",exp)
	return user_exp, exp

#step 2 : Check Validity of Expression

def validate_exp(n):
	print(n)
	#First Element and Last Element must operands 
	#First Element and Last Element must not be operator 
	max_index = len(n)-1
	if n[0] not in opr and n[max_index] not in opr :
		for i in range(1,max_index):
			if i%2==0 and n[i] in opr :
				print("Invalid Expression")
				break
		else :
			print("Valid Expression")
	else : 
		print("Invalid Expression")

class stack:
	def __init__(self):
		self.stack_list= []
		self.top = -1

	def push(self,x):
		self.stack_list.append(x)
		self.top = self.top + 1

	def pop(self) : 
		y = self.stack_list.pop()
		self.top = self.top - 1
		return y 

def convert_infix_postfix(exp) : 
	con_exp = []
	temp = stack()

	print("---------------------")
	for i in exp : 
		if i.isdigit():
			con_exp.append(i)
		else : 
			if temp.top == -1 :
				temp.push(i)
				print("Temp stack list", temp.stack_list)
				print("Converted List",con_exp)
			else : 
				for j in range(temp.top,0,-1):
					stack_top = temp.stack_list[temp.top]
					if opr[i] < opr[stack_top] :
						temp.push(i) 
						break
					else : 
						mid = temp.pop()
						con_exp.append(mid)
						temp.push(i)
						stack_top = temp.stack_list[temp.top]
						
	else :
		pass


	print("Before Conversion : ",exp)
	print("After Conversion : ", con_exp)
		


user_input, expr1 = expression()
#validate_exp(expr1)
convert_infix_postfix(expr1)