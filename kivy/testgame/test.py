def True_or_False(maybe):
    if maybe:
        print(maybe, ' is true')
    else:
        print(maybe, 'is false')
        
True_or_False([])
True_or_False([1])

class testing():
    def __init__(self):
        self.a = 1
        self.b = 1
        self.add = self.a + self.b

test = testing()
print (test.add)
test.b = 2
print (test.b , test.add)

print((((1,1)[0] +(1,1)[0]),((1,1)[1]+(1,1)[1])))

import random

for each in range(0,200):
    
    print(random.randint(0,2))