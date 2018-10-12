class Student:
	pr_raise=1.35
	def __init__(self,first,last,marks):         #always look in to the __init__ variable i.e (first,last,marks) 
		self.first=first
		self.last=last
		self.email=first+"."+last+"@gmail.com"
		self.marks=marks
		
	def fullname(self):
		return "{} {}".format(self.first,self.last)
	def intro (self):
		return "Hi! i am {} {}, my email address is {} and i have scored {} marks.".format(self.first,self.last,self.email,self.marks)
	def raiseApply(self):
		self.marks = int(self.marks * 1.35)

std1 = Student("Deniel","Stev",70)
std2 = Student("Mark", "Zukeberg",80)


print(std1.email)
print(std2.email)

print(std1.marks)
std1.raiseApply()
print(std1.marks)            #always look in to the __init__ variable i.e (first,last,marks) 

#print("{} {}".format(std1.first,std1.last))
print(std1.fullname())
print(std2.fullname())
print(std1.intro())
print(std2.intro())