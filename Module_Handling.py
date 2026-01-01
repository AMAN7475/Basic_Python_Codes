#Module Handling
import time

#Recursion Method

def fact(x):
	if x == 0 or x == 1:
		return 1
	else:
		return x * fact(x-1) 

A = int(input("Enter no of Iterations : "))
for B in range(A):
	rec_start_time = time.time()
	n = int(input("Enter Value : "))
	result = fact(n)
	print()
	print ("Factorial : ", result)
	rec_end_time = time.time()
	req_rec_time = rec_end_time - rec_start_time

	print("Recursion Time Data ")
	print("Start Time : ", rec_start_time)
	print("End Time : ", rec_end_time)
	print("Required Time : ",req_rec_time)
	print()
	
	#Iterative Method

	ite_start_time = time.time()
	fact_n = 1
	for i in range(1,n+1):
		fact_n = fact_n * i
	print()	
	print ("Factorial : ", fact_n)
	ite_end_time = time.time()
	req_ite_time = ite_end_time - ite_start_time

	print("Iterative Time Data")
	print("Start Time : ", ite_start_time)
	print("End Time : ", ite_end_time)
	print("Required Time : ",req_ite_time)
	print()