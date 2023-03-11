def validate(func):
    def validating(*args):
        for arg in args:
            if not isinstance(arg, int):

                return 'error'
            return func(*args)
    return validating
        
@validate
def add(a, b):
    return a + b



print(add(5, 7))   
print(add('3', 3)) 
print(add(1, 1.5))


'''
3.
write a function called validate(func), define a wrapper inside,
see if arguments were not integer, return and error.
define a function called add(a, b).
when calling the func add() in the end, if the args are integers return 
the sum, if even one of them in str, return that error you defined in the
first function.
'''