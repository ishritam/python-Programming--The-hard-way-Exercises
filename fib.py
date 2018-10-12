from functools import lru_cache
@lru_cache()

def fibonaci(n):
	if n ==1  or n==2:
		return 1
	elif n > 2:
		value= fibonaci(n-1) + fibonaci(n-2)
		return value
for i in range (1,1000):
	print(i ,fibonaci(i))