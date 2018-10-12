from sys import argv
script,user_name=argv
print(f"Hi {user_name}, I am {script}")
start_symbol =">"
print(f"What is your Nick Name {user_name}?")
nick=input(start_symbol)

print(f"Do you like me {nick}?")
like=input(start_symbol)

print(f"Do you wanna date with me {user_name}")
date = input(start_symbol)

print(f""" So, {user_name} Your Nick name is {nick} and your Liking choice is {like}, Your ans for date is {date}
             congratulation! you are in! """)