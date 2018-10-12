from sys import argv
script,user_name=argv
print(f"Hi {user_name}, I am {script}")
print(f"Tell me your nick name {user_name}:")
name=input(">>")
print(f"your age: {name}?")
age=input(">>")

print(f"Do you like me {name}?")
like=input(">>")

print(f""" Hi {user_name}, I am {script}
          your nickname is {name}
		  you are {age} years old
		  Liking is : {like}""")