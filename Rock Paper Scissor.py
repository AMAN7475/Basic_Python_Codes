"""a = "Rock"
b = "Paper"
c = "Scissor"

print("Rock Paper Scissor Game")
print("a = Rock")
print("b = Paper")
print("c = Scissor")

Repetitions = int(input("No. of games to be played : "))
S = (Repetitions/2)
R = ceil(S)

while R is False: 

	Player_1 = input("Player_1 ;Enter your choice : ")
	Player_2 = input("Player_2 ;Enter your choice : ")

	if Player_1 == Player_2:
		print("Its a Draw")

	elif Player_1 == a and Player_2 == c:
		print("Player 1 wins")	

	elif Player_1 == a and Player_2 == b:
		print("Player 2 wins")	

	elif Player_1 == b and Player_2 == a:
		print("Player 1 wins")

	elif Player_1 == b and Player_2 == c:
		print("Player 2 wins")	

	elif Player_1 == c and Player_2 == b:
		print("Player 1 wins")

	elif Player_1 == c and Player_2 == a:
		print("Player 2 wins")	

	else:
		print("Invalid Input")	

	R is True
	break"""

def f1(Player_1,Player_2):
	Player_1 == "Rock"
	if Player_2 == "Rock":	
		return ("Its a Draw")
	elif Player_2 == "Paper":		
		return ("Player_2 Wins")
	elif Player_2 == "Scissor":
		return ("Player_1 Wins")	

def f2(Player_1,Player_2):
	Player_1 == "Paper"	
	if Player_2 == "Paper":
		return ("Its a Draw")
	elif Player_2 == "Scissor":		
		return ("Player_2 Wins")
	elif Player_2 == "Rock":
		return ("Player_1 Wins")

def f3(Player_1,Player_2):
	Player_1 == "Scissor"	
	if Player_2 == "Scissor":
		return ("Its a Draw")
	elif Player_2 == "Rock":		
		return ("Player_2 Wins")
	elif Player_2 == "Paper":
		return ("Player_1 Wins")			

Iterations = int(input("How many times you want to play the game : "))
I = (Iterations/2)+1

Player_1_win_count = 0
Player_2_win_count = 0

while Player_1_win_count or Player_2_win_count <= I:	
	Player_1 = input("Player_1 Select one among Rock, Paper, Scissor : ")
	Player_2 = input("Player_2 Select one among Rock, Paper, Scissor : ")

	if Player_1 == "Rock":
		print("Result of game = {}".format(f1(Player_1,Player_2)))	

	elif Player_1 == "Paper":
		print("Result of game = {}".format(f2(Player_1,Player_2)))	

	elif Player_1 == "Scissor":
		print("Result of game = {}".format(f3(Player_1,Player_2)))

	break		