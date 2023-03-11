'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
# from https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-46.php

def amicable_sum(num):
	divisor_sum = [0] * num # makes list of 0's with num's length
	for i in range(1, len(divisor_sum)):
		for j in range(i * 2, len(divisor_sum), i):
			divisor_sum[j] += i	
	# Find all amicable pairs 
	result = 0
	for i in range(1, len(divisor_sum)):
		j = divisor_sum[i]
		if j != i and j < len(divisor_sum) and divisor_sum[j] == i:
			result += i
	return str(result)

print(amicable_sum(10000))
        
        
    