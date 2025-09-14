import random
l=[1,2,3,4,5]
print("Random number=",random.choice(l))
r=random.seed(5)
print("Random seed of number:",r)
print("Random integer number:",random.randint(1,5))
##print("Random number using random function:",random())
print("In list:",random.sample(l,3))
print("In shuffle:",random.shuffle(l))