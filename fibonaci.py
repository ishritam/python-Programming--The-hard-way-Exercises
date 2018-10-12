
def fibonaci(n):
	if n==1 or n==2:
		return 1
	elif n >2:
		return fibonaci(n-1)+fibonaci(n-2)
for i in range(1,10):
	print(i,":",fibonaci(i))