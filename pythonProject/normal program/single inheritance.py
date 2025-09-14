class Students:
    def accept(self):
        self.name=input("Enter a Name")
        self.marks=int(input("Enter a Marks"))
class Marks(Students):
    def show(self):
        print("name of Students:",self.name)
        print("marks of Students:",self.marks)
s=Marks()
s.accept()
s.show()