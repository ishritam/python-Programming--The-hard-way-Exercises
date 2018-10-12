def student(name,age):
	print(f"hi{name}, you are {age} years old.")        #print something to shown when the function is called
student("Shritam",19)


name="Shreet"   
age=20
student(name,age) #it will call the function "student" and print as per the var declared



first=20
second=30
student(first+20,second+10)  #you can add to the variable ,but print as you define the student --> Line2

student("Shritam","19+")
print(f"{name}{age}")