car = 100
x = f"there are {car} number of cars in his showroom" #here a variable(variable car) is use inside variable x 
suzuki="Hi! i am Suzuki {}"  #you have to give a empty string "{}" in the end of the string to call it (using ".format")
suzuki_1 = f"Hi! i am Suzuki, and i have {car} models "
maruti= "and i have one showroom in sambalpur"

print(x)
print(suzuki.format(maruti))   #by using ".format" we can mearge both variables (i.e string inside a string)
