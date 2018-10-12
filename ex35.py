def gold_room():
	print("It's a room full with Gold.")
	print("Chose how many coin do you want?")
	choice= int(input(">>"))
	if choice <50:
		print("You are not a greedy person. Well done.")
		print("You Won! Congratulation.")
	elif choice > 50:
		print("You are a greedy basted MF. Go to hell.")
		tiger()
	else:
		print("Man! You need a school first.")
def tiger():
	print("There is no place for greedy people in this Universe")
	game_over()
def bear_room():
	print("There is a single room for the exist. And the bear is sleeping in front of it. He has a Honey pot.")
	print("Choice is your's. You are Surviving for many days in this shell.")
	bear_move=False
	print(""" 1. Through a Stone to him.\n2. Grave the honey pot from him.\n3. Try to distract him.""")
	choice = int(input(">>"))
	if choice == 1:
		print("You are a Fool. He will never let you go.")
		game_over()
		
	elif choice ==2 and not bear_move:
		print("Ready for Hug Bear Slap.")
		bear_move = True
		bear_room()
		
	elif choice== 1 and bear_move:
		bear_room()
	elif choice == 3:
		print("Great job Man. Now you have an opportunity to take the Golds.")
		gold_room()
def game_over():
	print("******************************GAMEOVER********************************")
def tchulhu():
	print("there is a huge evil Tchulhu.")
	print("Choice is up to you, Flee or Say eat",end = ".")
	choice = input(">>")
	if choice == "Flee" or choice == "flee" or choice =="FLEE":
		print("Good. Now you are safe from the evil Gent. Go for Gold.")
		gold_room()
	elif choice == "eat" or choice == "Eat":
		print("Well,For Tchulhu it was testy")
		game_over()
	else:
		print("Choose a valid Choice or you will die soon.")
		tchulhu()
def start():
	print("You have two Doors. Left or Right.")
	choice = input("Enter your Choice >>")
	if choice == "Left":
		bear_room()
	elif choice == "Right":
		tchulhu()
	else:
		print("Choose from Left and Right")
		start()
start()
		