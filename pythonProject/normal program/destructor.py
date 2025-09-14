class students:
    def __init__(self):
        print("I am in constructor")
    def __del__(self):
        print("I am in destructor")
s=students()
