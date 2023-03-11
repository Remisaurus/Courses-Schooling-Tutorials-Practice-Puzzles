# built-in functions

>>> max('Hello world')
'w'
>>> min('Hello world')
' '

>>> len('Hello world')
11

>>> int(3.99999)
3
>>> int(-2.3)
-2

>>> float(32)
32.0
>>> float('3.14159')
3.14159

import random
for i in range(10):
x = random.random()
print(x)

random.randint(5, 10)

>>> t = [1, 2, 3]
>>> random.choice(t)
2
>>> random.choice(t)
3

# new functions

def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Johnson")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Johnson")

def my_function(country):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function("Brazil")

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# Exercises

Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
(hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
