#import time
#import time as t # aliasing 
from time import time 

def facts(x):
	if x == 0 or x == 1 :
		return 1
	else : 
		return x * facts(x-1)

#iterative method 

x = int(input("Enter Value : "))
print("=======================")
print("Iterative Method Result")
start_time1 = time()
fact = 1 
for i in range(1,x+1):
	fact *= i
print("Factorial of {} = {}".format(x,fact))
end_time1 = time()

total_time1 = end_time1 - start_time1 

print("Start Time : ",start_time1)
print("End Time : ",end_time1)
print("Total Time : ",total_time1)
print("=======================")


#recursive 
print("=======================")
print("Recurssive Method Result")
start_time2 = time()
fact = facts(x)
print("Factorial of {} = {}".format(x,fact))
end_time2 = time()

total_time2 = end_time2 - start_time2 

print("Start Time : ",start_time2)
print("End Time : ",end_time2)
print("Total Time : ",total_time2)
print("=======================")






