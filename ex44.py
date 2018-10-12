class Parent(object):
	def altered(self):
		print("PARENT altered()")
	
class Child(object):
	def __init__(self):
		self.parent = Parent()
	def altered(self):
		print("CHILD before super function")
		#super(Child,self).altered()
		print("CHILD after super function")
Father = Parent()
Son = Child()


Father.altered()
Son.altered()