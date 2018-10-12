def operation(a,b,op):
	if op=="add":
		return a+b
	elif op=="sub":
		return a-b
	elif op=="mult":
		return a*b
		
print(__name__)
if __name__=="__main__":
	print(operation(2,5,"add"))
	print(operation(5,2,"sub"))
	
