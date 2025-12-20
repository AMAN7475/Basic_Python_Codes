from time import time
from functions import *

file = open("sample.txt","a")
for i in range(1,10):
	initial_time1 = time()
	result_iter = Iterative_Method(i)
	final_time1 = time()

	initial_time2 = time()
	result_recur = Recursion_Method(i)
	final_time2 = time() 

	iter_time = final_time1 - initial_time1

	recur_time = final_time2 - initial_time2

entry = "{},{},{},{}".format(i,result_iter,iter_time,recur_time)	


file.write(entry)
file.close()

