class Car(object):
	run= False
	def __init__(self,name,color,model,year):
		self.name = name
		self.color = color
		self.model = model
		self.year = year
		
	def accelerator(self):
		print("Car is speeding up...")
		self.run=True
		
	def brake(self):
		if self.run==True:
			print("Car is speeding down...")
			self.run=False
		else:
			print("Car has already been stopped...")
	def left(self):
		if self.run==True:	
			print("Car is turning left...")
		else:
			print("Car has already been stopped...")
	def right(self):
		if self.run==True:	
			print("Car is turning Right...")
		else:
			print("Car has already been stopped...")
		
		
class Super_car(Car):
	def N2o(self):
		Road = input("Fine or Rough ??")
		if Road == "fine":
			print("Enjoy the High speeding N2o..........")
		elif Road=="rough" or Road=="Rough":
			print("Find a fine road then only i can Permit you!")
		else:
			print("Choose anyone of these")
			
car1= Car("Mahendra","Red","XUV500","2014")
car2 = Super_car("Lemborgini","Yellow","Venitro","2015")
car1.accelerator()
car1.brake()
car1.brake()

print("*"*10)
car2.accelerator()
car2.brake()
car2.brake()

car2.right()