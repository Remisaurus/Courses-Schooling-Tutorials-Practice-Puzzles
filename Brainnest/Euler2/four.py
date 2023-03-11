'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''
'''
For speedy resolve the site:
' https://radiusofcircle.blogspot.com/2016/05/problem-34-project-euler-solution-with.html '
has been consulted.
'''

#factorial function for calculating factorial (digit!)
from math import factorial 

#factorials of numbers from 0-9
factorials = [factorial(0), factorial(1), factorial(2), factorial(3), factorial(4),
factorial(5), factorial(6), factorial(7), factorial(8), factorial(9)]

#sum of factorial of the digits (as found in https://stackoverflow.com/questions/974952/split-an-integer-into-digits-to-compute-an-isbn-checksum/975039#975039)
def factorial_digits(n):
    value = 0
    while n:
        value += factorials[n % 10]
        n //= 10 # n = n // 10 (// is floor division).
    return value

#variable to save the value of solution
solution = 0

#for loop to loop till 1854721 (as found with https://en.wikipedia.org/wiki/Factorion)
for i in range(10,1854721):
	if factorial_digits(i) == i:
		solution += i

#printing the solution
print(solution)
