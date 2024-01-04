#Random Number Generation
import random
x=random.random()#only between 0 and 1 excluded
print(x) #==> Gives ouput between the range [0,1)
y=random.randint(10,20) #Both 10 and 20 included gives random integer
print(y)
z=random.uniform(3,5) # gives random floating number
print(z)
