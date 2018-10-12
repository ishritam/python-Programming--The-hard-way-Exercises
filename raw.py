array = "fridge cooler A/c Bike"
a= array.split(' ')
new = ["Dog","Cat","Well","Tree","Cow","Orange","Floor","Cow-house"]
while len(a)!= 10:
	b=new.pop()
	a.append(b)
	print("\a")
print(a)
#print(f"There are {len(a)} iteams now.}")
#print(a)
print('#'.join(a))
print(','.join(a))