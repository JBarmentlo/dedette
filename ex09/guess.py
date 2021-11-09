nb = input("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\nWhat's your guess between 1 and 99?\n")
secret_nb = 11
trials = 1
l = 0
if (nb == str(secret_nb)):
	print("Congratulations! You got it on your first try!")
while (nb != str(secret_nb)):
	if (nb == "exit"):
		break
	try:
		nb = int(nb)
		if nb < 11 and nb != 42:	
			nb = input("Too low!\n")
			trials += 1
		elif nb > 11 and nb != 42:
			nb = input("Too high!\n")
			trials += 1
		elif nb == 42:
			nb = input("The answer to the ultimate question of life, the universe and everything is 42, but it is not the good guess....\nTry again:\n")
			trials += 1
	except ValueError:
		nb = input("That's not a number.\nWhat's your guess between 1 and 99?\n")
if (nb == str(secret_nb)):
	print(f"Congratulations, you've got it!\nYou won in {trials} attempts!")