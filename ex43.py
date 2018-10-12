class Car:
	carMoving = False
	def __init__(self,name,model,fuel,seat):
		self.name = name
		self.model = model
		self.fuel = fuel
		self.seat = seat
		
	def accelerator(self):
		self.carMoving= True
		print("Car is speeding up...",self.model)
	def Brake(self):
		if self.carMoving:
			print("car is slowing down...")
			self.carMoving = False
		else:
			print("Car has been stopped...")
	def turnLeft(self):
		print("Car is turning Left.....")
	def turnRight(self):
		print("car is turning Right......")
		
	def changeOil(self):
		print("Oil has been changed...")
		
#	def __var(self,change):
#		self.__carChange = change
#		print("Number of time car changed owner",__carChange)
		
class sportCar(Car):           #inheritance from the parent class by is_a relationship
	def input(self):
		speed = input("\n.........Electric or Diesel\n>>\t")
		if speed=="Electric":
			print("Fine road..TIME TO FLY.......")
		elif speed=="Diesel":
			print("Normal road..DRIVE IN NORMAL SPEED")
		else:
			print("Always take left and slow your speed.....")
#	def __init__(self,name,model):
#		self.name = name
#		self.model = model
	print("Supercar.............car")
			
car1=Car("Mahendra","XUV500","Diesel","7")
sportCar1 = sportCar("BMW","F1","Diesel","7")
print(sportCar1.name)
sportCar1.accelerator()
sportCar1.input()
sportCar1.Brake()
sportCar1.Brake()
sportCar1.Brake()
print("*"*10)
#car1.__var("10")



print("*"*10)
print(car1.name)
car1.accelerator()
car1.Brake()
car1.Brake()
car1.Brake()