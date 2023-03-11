'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
'''
for speedier resolve of the problem the site:
' https://radiusofcircle.blogspot.com/2016/05/problem-33-project-euler-solution-with-python.html '
has been consulted.
'''

from fractions import Fraction

product = 1
result_list = []

for i in range(10,100):
    for j in range(i+1,100): # denominator > nominator, so i+1, 100
        common = list(set(str(i))&set(str(j))) # looking if the figures have a common mumber
        if len(common) != 0: # checking if the list is (not) empty
            if common[0] != '0': # checking if the common number is not 0
                num = list(str(i))
                den = list(str(j))
                #Remove the common element from numerator
                num.remove(common[0])
				#Remove the common element from Denominator
                den.remove(common[0])
                if num[0] != '0' and den[0] != '0': # checking if the value of num and den are not equal to 0
                    if Fraction(int(num[0]),int(den[0])) == Fraction(i,j): # seeing if they are equal
                        product *= Fraction(i,j)
                        result_list.append([i, j])

print(product.denominator)
print(result_list)

