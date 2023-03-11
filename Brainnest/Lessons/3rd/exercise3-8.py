# a + b + c = 1000
# a ** 2 + b ** 2 = c ** 2

# c = 1000 - (a + b)

# a ** 2 + b ** 2 = (1000 - (a + b)) ** 2

n = 50

n_list = []
for each in range(1, n+1):
    n_list.append(each)
    
for a in n_list:
    print(a)
    for b in n_list:
        if a ** 2 + b ** 2 == (1000 - (a + b)) ** 2:
            print (f'found solution: a and b are: {a} and {b}. which makes c: {1000 - (a + b)}.')
            break
        
# not finished


