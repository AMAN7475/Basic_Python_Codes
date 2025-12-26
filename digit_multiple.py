"""num = int(input("Enter Number:"))
x = num
multiple = 1
while x != 0 : 
	multiple = multiple * (x%10)
	x = x //10
print(multiple)"""


num = int(input("Enter Number:"))
x = num
multiple = 1
for i in range(x,0,-1): 
	multiple = multiple * (x%10)
	x = x // 10 
	print(x)
	print(multiple)