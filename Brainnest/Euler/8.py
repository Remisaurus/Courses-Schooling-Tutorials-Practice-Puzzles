'''A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient
if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.'''

N = 28125

result_list = []
abundant_numbers = []
perfect_numbers = []
deficient_numbers = []
sum_list = []
integers_list = []

for each in range (1, N):
    integers_list.append(each)

for each in range(11, N): # abundant numbers start from 12 so below that is not neccesary for this assignment.
    divisor_list = []
    for numbers in range(1, int(0.5 * each) + 1):
        if each % numbers == 0:
            divisor_list.append(numbers)
    result = 0
    for every in divisor_list:
        result += every
    if result > each:
        abundant_numbers.append(each)
    elif result < each:
        deficient_numbers.append(each)
    elif result == each:
        perfect_numbers.append(each)
        
for numbers in abundant_numbers:
    print(numbers)
    for addition in abundant_numbers:
        current = numbers + addition
        if current > N:
            break
        if current not in sum_list:
            sum_list.append(current)
            
for each in integers_list:
    if each not in sum_list:
        result_list.append(each)
        
print(result_list)

    
    
         