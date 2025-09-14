class Circle:
      pi=3.14
      def __init__(self,r):
        self.r=r
      def area(self):
        print(Circle.pi*self.r*self.r)
area=Circle(5)
area.area()        
       