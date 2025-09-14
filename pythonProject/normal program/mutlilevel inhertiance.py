class A:
    def show(self):
        print("I am in A")
class B(A):
    def B(self):
        print("I am in B")
class C(B):
    def C(self):
        print("I am in C")
a=C()
a.B()
a.show()
a.C()

