'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
'''
this too is a too hard problem for me to do alone. therefore, internet has been used to solve it.
(https://www.educative.io/answers/how-to-solve-the-project-euler-32-problem)
I will add some comments to show I understand the code.
'''

sumC = 0
alreadyFound=[]

# Since a valid answer should be using 9 digits only 2x3=4 and 1x4=4 combinations have to be considered.

# CASE 1. (a - 2-digit) and (b - 3-digit) 
upperA = 98
upperB = 987
# loop within loop creates all possible combinations
for a in range(9,upperA+1):
    for b in range(98,upperB+1):
        c = a*b
        if len(str(c))>5: break # filters out non 9 length combinations
        
        allDigits = sorted(str(c)+str(a)+str(b))
    
        if allDigits == list('123456789') : # see if the sorted list is 123456789
            if c not in alreadyFound :
                alreadyFound+=[c] # add the result to the already found list (if not already in there)
                sumC+=c


# CASE 2. (a - 1-digit) and (b - 4-digit) 
upperA = 9
upperB = 9876
# loop within loop creates all possible combinations
for a in range(1,upperA+1):
    for b in range(987,upperB+1):

        c = a*b
        if len(str(c))>5: break # filters out non 9 length combinations
        
        allDigits = sorted(str(c)+str(a)+str(b))
    
        if allDigits == list('123456789') : # see if the sorted list is 123456789
            if c not in alreadyFound :
                alreadyFound+=[c] # add the result to the already found list (if not already in there)
                sumC+=c


print(alreadyFound)
print(sumC)