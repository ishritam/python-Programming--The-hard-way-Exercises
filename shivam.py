# from functools import lru_cache
# @lru_cache()

b=4
c=3

d=5
e=4


f=6
g=5
print("For a")
for i in range(100):
	
	if i%b==c:
		print(f"{i}",end=",")
print()
print("for b")
for i in range(200):
	
	if i%d==e:
		print(f"{i}",end=",")
print()
print("for c")

for i in range(200):
	
	if i%f==g:
		print(f"{i}",end=",")