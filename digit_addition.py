num = int(input("Enter Number : "))
sum_digits = 0

for i in str(abs(num)):
	sum_digits = sum_digits + int(i)

print("Sum of Digits : " ,sum_digits)