def greet(func):
     
    def print_me(*args):
       
        print("me")
        return func(*args)
    
    return print_me()
        
def say_hello():
    print('hello')
    
greet(say_hello)


'''
1.
write a function named greet(func)

inside greet(func) create another function that does the following:
	1. print something
	2. a variable that uses func to access different arguments (*args)

define another function called say_hello() which prints something
and by calling say_hello() at the end, also the greet(func) should be
provoked.
'''