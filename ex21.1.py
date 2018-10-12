#24 + 34 / 100 - 1023

def add(a,b):
	return a+b 
def sub(a,b):
	return a-b 
def div(a,b):
	return a / b 


a=24
b= 34
c=100
d = 1023

new= div(add(a,b),sub(c,d))

print(f"{new}")