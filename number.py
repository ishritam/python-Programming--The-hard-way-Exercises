from functools import lru_cache
@lru_cache()
def fib(n):
	if n==1 or n==2:
		print(1)
	elif n>2:
		print(fib(n-1)+fib(n-2))
for i in range(1,100):
	print(f"{i} : {fib(i)}")