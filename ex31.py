print("""You'r in a dungeon!
        You have Two gates. Chose any one: #1 or #2
		And both door has a Diamond""")
gate = input(">")

if gate == "1":
	print("There is a Bear.")
	print("he is eating Cake.")
	print("""Choice is up to you Chose Cake or Diamond""")
	print("1: Cake")
	print("2: Diamond")
	choice1= input(">>")
	if choice1 == "1":
		print("You are hungry and Fool.")
	elif choice1 == "2":
		print("You are brave! Let the bear eat and still the Diamond.Good Job!")
	else:
		print("Wait until he finishes the cake, after he'll kill you")
elif gate == "2":
	print("There is a Hug snake, and he's sleeping.")
	print("The diamond is on the top of his haad")
	print("""Choice is up to you Chose Cake or Diamond""")
	print("1: Cake")
	print("2: Diamond")
	choice2 = input(">>")
	if choice2 =="1":
		print("You are brave. You can't take the diamond from the snakes head. Good Job!")
		print("Nice")
	elif choice2 =="2":
		print("You can't take the diamond from the snakes head.")
		print("if you selected it, You are a fool, you gonna die.")
	else:
		print("Wait until he finishes his sleep, after he'll kill you")
else:
	print("There are blade around you. They will cut your body. chose a door for you #1 or #2")