x = "a young girl walked into a library with an old, tattered book in her hand. She was searching for a quiet corner to read, but the noise from a nearby group distracted her. The librarian, noticing her struggle, pointed to a secluded section behind the large shelves. There, she found an empty chair and a wooden table with a small lamp. As she flipped through the pages, she discovered a hidden note between the chapters — a message from an unknown author who had visited the library years ago. The mystery intrigued her, and she decided to spend the afternoon solving the clues left behind."

count_a = 0
count_an = 0 
count_the = 0

for i in range(len(x)):

	if x[i] == "a" and x[i-1] == " " and x[i+1] == " ":
		count_a += 1

	elif i == 0 and x[i] == "a" and x[i+1] == " ":
		count_a += 1

for j in range(len(x)):

	if x[j] == "a" and x[j:j+2] == "an" and x[j-1] == " " and x[j+2] == " ":
		count_an += 1

	elif j == 0 and x[j:j+2] == "an" and x[j+2] == " ":
		count_an += 1				

for k in range(len(x)):

	if x[k] == "t" and x[k:k+3] == "the" and x[k-1] == " " and x[k+3] == " ":
		count_the += 1

	elif k == 0 and x[k:k+3] == "the" and x[k+3] == " ":
		count_the += 1


print("count_a",count_a)
print("count_an",count_an)	
print("count_the",count_the)	