'''
this is a complicated mathmatical problem.
some pages should be considered for the solution and to understand the code:
https://blog.dreamshire.com/solutions/project_euler/project-euler-problem-026-solution/
https://mathworld.wolfram.com/FullReptendPrime.html 

The time it would take to grasp the problem and write own code to solve it would take a long time.
'''

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]
def f(N):
    if N <= 7: return 3
    for d in prime_sieve(N)[::-1]:
        k = d//2
        while pow(10, k, d) != 1: k+= 1
        if d-1 == k: return d
  
N = int(input('The longest recurring cycle for 1/d where d < '))
d = f(N)
print ("The longest repeating decimal for d < %d is 1/%d with %d repeating digits" % (N, d, (1 if N<8 else d-1)))
