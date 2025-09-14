x=('zero','one','two','three','four','five','Six','seven','eight','nine')
b=[]
number=int(input("Enter a number"))
while number>0:
    r=x[number%10]
    number=int(number/10)
    b.append(r)

b.reverse()
print(b)