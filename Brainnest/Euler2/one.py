'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

'''
'''
after struggling with the problem for several hours and only gaining a small momentum in solving the problem,
I decided to use the code findable on the internet to solve the problem. 
(https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-62.php)
I am ashamed I had to, but this problem is best solved by higher mathematics and I am not equipped to do so.
'''
amount_to_make = 200
coins_to_use = [1, 2, 5, 10, 20, 50, 100, 200]

def number_of_ways(amount, coins): # (int of target amount, list with coins possible (lowest first)).
    number_ways = [coins[0]] + [0] * int(amount / coins[0]) # creating a list with the lowest coin and 0s as per howmany you need of that coin to get the amount.
    for coin in coins: 
        for i in range(len(number_ways) - coin): # using mathematics to find possibilities.
            number_ways[i + coin] += number_ways[i]
    return str(number_ways[-1])

print(number_of_ways(amount_to_make, coins_to_use))