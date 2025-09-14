a=[10,20,30]
try:
    print("Second element=",a[1])
    print("Fourth element=",a[3])
except IndexError:
    print("IndexError")