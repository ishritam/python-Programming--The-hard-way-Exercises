print("Exercise33")

numbers =[]

def function(i):
	for num in range(i,6):
		print(f"Value of i at the top: {num} ")
		print(numbers)
		numbers.append(num)
		num=num+1
		print(f"Value of i at the bottom {num}")
		print("*"*20)
function(0)
for num in numbers:
	print(num)
