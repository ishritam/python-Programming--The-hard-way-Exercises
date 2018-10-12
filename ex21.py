def add(a,b):
	return a + b
	
def sub(a,b):
	return a - b
	
def mult(a,b):
	return a * b

def div(a,b):
	return a / b
	
addition = add(10, 10)
substract= sub(10,10)
multiplication = mult(10, 10)
division = div(10,10)

puzzel = add(addition,sub(substract,mult(multiplication,div(division,1))))
#puzzel = add(add(10,10),sub(sub(10,10),mult(mult(10, 10),div(div(10,10),1))))
#puzzel = add(add(10,10),sub(sub(10,10),mult(mult(10, 10),div(1,1))))
#puzzel = add(add(10,10),sub(sub(10,10),mult(mult(10, 10),1)))
#puzzel = add(add(10,10),sub(sub(10,10),mult(mult(100,1))))
#puzzel = add(add(10,10),sub(sub(10,10),100))
#puzzel = add(add(10,10),sub(0,100))
#puzzel = add(add(10,10),-100))
#puzzel = add(20,-100)
#puzzel = -80
print(f"{puzzel}")	

print("\a")