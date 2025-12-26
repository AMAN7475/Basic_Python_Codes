def reverse_digit(n):
	reverse_num = 0
	while n > 0:
		digit = n % 10
		reverse_num = reverse_num * 10 + digit
		n = n // 10

	return reverse_num	


x = int(input("Enter a positive integer : "))
if x <= 0:
	print("Exiting")

else:
	result = reverse_digit(x)

print("Reversed Digits of {} = {}".format(x,result))	
