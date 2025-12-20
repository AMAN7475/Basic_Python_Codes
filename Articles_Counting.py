"""file = input("Enter your text : ")
article_count = 0

for i in (file):
	if i == "a" or i == "an" or i == "the":
		article_count += 1	

print ("The no. of articles = ", article_count)"""


n = input("Enter The Text:")
Total_article_count = 0
Count_a = 0
Count_an = 0
Count_the = 0

x = n.split()
for i in x:
	if i.lower() == "a" or i.upper() == "a":
		Count_a += 1
		Total_article_count += 1

	elif i.lower() == "an" or i.upper() == "an":
		Count_an += 1
		Total_article_count += 1

	elif i.lower() == "the"	or i.upper() == "the":
		Count_the += 1
		Total_article_count += 1

print ("Total no. of articles = ", Total_article_count)
print ("No. of article (a) = ", Count_a)
print ("No. of article (an) = ", Count_an)
print ("No. of article (the)", Count_the)