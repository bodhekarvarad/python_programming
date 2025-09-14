class Rectangle:
    def __int__(self):
        print("for a Rectangle")
        self.len=int(input("Enter a length"))
        self.width=int(input("Enter a breadth"))
    def logic(self):
        self.area=self.len*self.width

class Square:
    def accept(self):
        print("for square")
        self.side=int(input("Enter side"))
class Show(Rectangle,Square):
    def show(self):
        print("Area of rectangle",self.area)
        print("Area of square",self.area*2)
s=Show()
s.__int__()
s.logic()
s.accept()
s.show()

