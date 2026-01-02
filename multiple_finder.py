start = int(input("Enter start Value :"))
end = int (input("Enter end Value :"))
multiple = int (input("Enter multiple value :"))
for i in range (start,end+1) :
	if i%multiple == 0 :
		print (i)