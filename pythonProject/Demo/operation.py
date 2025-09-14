class A:
    def __int__(self):
        self.num=int(input("Enter a Num1"))
        self.num2=int(input("Enter a Num2"))
    def add(self):
        print("Addition=",self.num+self.num)
    def sub(self):
        print("Subtraction=",self.num-self.num2)
a=A()
a.__int__()
a.add()
a.sub()