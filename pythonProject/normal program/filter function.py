def odd(num):
    if num %2!=0:
        return True
li=[1,2,3,4,5,89,79]
res=list(filter(odd,li))
print(res)