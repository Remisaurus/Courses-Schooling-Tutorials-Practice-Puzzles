primelist = []

def is_prime():
    global primelist
    if len(primelist) == 0:
        x = 3
    else:
        x = primelist[-1]
    def get_next(x):
        if len(primelist) == 0:
            primelist.append(2)   
        else:
            if x % 2 == 0:
                x += 1
                get_next(x)
                return
            for every in primelist:
                if x % every == 0:
                    x += 1
                    get_next(x)
                    return
        primelist.append(x)
    get_next(x)


def prime_numbers(n):
    count = 0
    while count < n:
        is_prime()
        count += 1
       


prime_numbers(9)
print(primelist)
    

'''
1.
write a function that yields the first 10 prime numbers.

Tips:
	you need 2 functions (is_prime() and prime_numbers(n)) 
	
prime_generator = prime_numbers(10)
print(list(prime_generator))

# output should be:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
'''