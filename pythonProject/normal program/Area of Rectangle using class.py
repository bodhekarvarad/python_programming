class Rectangle:
    def __init__(self,a,b):
        self.l=a
        self.b=b
    def area(self):
        print("Area:",self.l*self.b)
rec=Rectangle(6,6)
rec.area()