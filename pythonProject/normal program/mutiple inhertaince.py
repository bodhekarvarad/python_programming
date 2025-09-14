class A:
    def method1(self):
        print("I am in method1")
class B(A):
    def method2(self):
        print("I am in method2")
class C(B):
    def method3(self):
        print("I am in method3")
c=C()
c.method1()
c.method3()
c.method2()