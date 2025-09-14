class Students:
    def __int__(self):
       self.a=int(input("Enter a number"))
    def show(self):
        print("Number is:",self.a)
s=Students()
s.__int__()
s.show()