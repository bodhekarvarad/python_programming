class Students:
     def __init__(self,n,a,g):
	    self.name=n
		self.age=a
		self.gendre=g
	def show(self):
	    print("Name of students:",self.name)
		print("Age of Students:",self.age)
		print("Gendre of Students:".self.gendre)
s=Students("Varad",18,"Male")
##s.__init__("Varad",18,"Male")
s.show()