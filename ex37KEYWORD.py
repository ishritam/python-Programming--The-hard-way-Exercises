1) With_as
--------------

with open('pythonText.txt','w') as var:
	var.write("Hello new file")                    #It will creat a File name as pythonText.txt first and then write Hello new file in pythonText.txt

2) assert
------------

def _age():
	i_age = int(input("How old are you? >>"))
	assert i_age > 0 , "Age can't be Negative."
	print(f"Ok, You are {i_age} years old")
	
_age()


OUTPUT
******
D:\Python>ex37.py
How old are you? >>-19
Traceback (most recent call last):
  File "D:\Python\ex37.py", line 6, in <module>
    _age()
  File "D:\Python\ex37.py", line 3, in _age
    assert i_age > 0 , "Age can't be Negative."
AssertionError: Age can't be Negative.

3) class
---------------

class Calculator:
	def add():
		a = int(input("First Number >>"))
		b = int(input("Second Number >>"))
		print(a + b)
	def sub():
		a = int(input("First Number >>"))
		b = int(input("Second Number >>"))
		print(a - b)
Calculator.add()
Calculator.sub()
	


4) Break
------------------
number = 0
for number in range(10):
	number = number + 1
	
	if number == 5:
		break      #for break a statement
	print(number)

print("Out of the loop")
print(number)


5) del
---------------

a = [1,2,3,4,5]
del a[2]
print(a)

D:\Python>ex37.py
[1, 2, 4, 5]


6) try:.............except:
--------------------------------

import math
num = int(input("Enter the number you want to see the Fatorial:>>"))

try:
	result = math.factorial(num)
	print(result)
except ValueError:
	print("Negative number is not allowed.") 