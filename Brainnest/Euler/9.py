'''
This exercise is fairly simple with the import of the itertools library.
'''
import itertools


def lexicographic(number, digits): # digits should be a string, returns number's permutation.
    return list(itertools.permutations(digits))[number - 1]


permutation = list(lexicographic(1000000, '0123456789'))
print(''.join(permutation))