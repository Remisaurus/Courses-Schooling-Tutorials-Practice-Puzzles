'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
'''
For this exercise the site:
' https://www.geeksforgeeks.org/circular-primes-less-than-n/ '
was consulted
'''
result_list = []

# using Sieve of Sundaram.
 
def circularPrime(n):
    # In general Sieve of Sundaram,
    # produces primes smaller than
    # (2*x + 2) for a number given
    # number x. Since we want primes
    # smaller than n, n is reduced by half
    nNew = (n - 2) // 2
  
    # This array is used to separate numbers
    # of the form i+j+2ij from others
    # where 1 <= i <= j
    marked = [False for i in range(nNew + 1)]
    
    SieveOfSundaram(marked, nNew)
  
    # If n > 2 then 2 is also a
    # circular prime
    result_list.append(2)
  
    # According to Sieve of sundaram
    # If marked[i] is false then
    # 2*i + 1 is a prime number.
  
    # Loop to check all  prime numbers
    # and their rotations
    for i in range(1, nNew + 1):
     
        # Skip this number if not prime
        if (marked[i] == True):
            continue
  
        num = 2 * i + 1
         
        # Function for rotation of prime
        num = Rotate(num)
         
        # Now we check for rotations of this
        # prime number if new rotation is
        # prime check next rotation, till
        # new rotation becomes the actual
        # prime number and if new rotation
        # if not prime then break
        while (num != 2 * i + 1):
             
            # Check for even
            if (num % 2 == 0):
                break
  
            # If rotated number is prime
            # then rotate for next
            if (marked[(num - 1) // 2] == False):
                num = Rotate(num)
            else:
                break
 
        # If checked number is circular
        # add it to list
        if (num == (2 * i + 1)):
            result_list.append(num)
 
# Sieve of Sundaram for generating
# prime numbers
def SieveOfSundaram(marked, nNew):
 
    # Main logic of Sundaram. Mark
    # all numbers of the form
    # i + j + 2ij as true where 1 <= i <= j
    for i in range(1, nNew + 1):
        j = i
        while (i + j + 2 * i * j) <= nNew:
            marked[i + j + 2 * i * j] = True
            j += 1
             
# Rotate function to right rotate
# the number
def Rotate(n):
     
    # Find unit place number
    rem = n % 10
     
    # To put unit place
    rem = rem * (10 ** (countDigits(n) - 1))
     
    # Number as first digit.
    n = n // 10 # Remove unit digit
    n += rem # Add first digit to rest
    return n
 
# Function to find total number of digits
def countDigits(n):
 
    digit = 0
     
    while n != 0:
        n = n // 10
        digit += 1
         
    return digit
 
# Driver code
if __name__=="__main__":
     
    n = 10 ** 6
     
    circularPrime(n)
    print(result_list, '\n', f'total number of circular primes under {n} = {len(result_list)}')
    
 