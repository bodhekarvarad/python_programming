import functools
def add(x,y):
    return(x+y)
list1=[1,11,2,3]
res=functools.reduce(add,list1)
print(res)