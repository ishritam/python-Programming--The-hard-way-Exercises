print("Hi there!")
name ="I am Shritam Kumar Mund {}"

user="Shritam"
age = 14
school = "ssvm dharamgarh"

print(name.format(age))
print(name.format(school))

print("." *30)  #it will print ten dots in a line
print("My Father Name is:")
c1 = "S."
c2 = "D"
c3= " "
c4 = "Mund"
print(c1 + c2, end=' ')   #here the -->,end='' operator is use to give a space in the end
#print(c1 + c2, c=' ')----> only end='' can be use
print(c4)

x = "week"
print("The is the beginning of the {} {}".format('Week',2))
print(f"This is the beginning of the {x}")

print("I am {}".format(user), end='.') #it will merge the two sentence with a "." operator in the middle.
print(f"I am {age} years old", end='.')