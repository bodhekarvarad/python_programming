try:
    a=15/0
    print(a)
    print("B=",b)
except ArithmeticError:
    print("Arithmetic Error")
except NameError:
    print("Name Error",b)