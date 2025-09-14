class Students:
	def __int__(self,n="Varad",a=18,g="Male"):
		self.name=n
		self.age=a
		self.gender=g
	def show(self):
		print("Name of Students:",self.name)
		print("Age of Students:",self.age)
		print("Gender of Students:",self.gender)
s=Students()
s.__int__()
s.show()
