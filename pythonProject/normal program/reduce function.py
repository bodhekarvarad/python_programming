import functools
def add(x,y):
    return (x+y)
li=[11,22,33,44,55,66]
res=functools.reduce(add,li)
print(res)