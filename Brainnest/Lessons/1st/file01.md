# values and types 

>>> print(4)
4

>>> type('Hello, World!')
<class 'str'>
>>> type(17)
<class 'int'>

>>> type(3.2)
<class 'float'>

>>> type('17')
<class 'str'>
>>> type('3.2')
<class 'str'>

>>> print(1,000,000)
1 0 0

c = True
print(c) # Output: True
print(type(c)) # Output: <class 'bool'>

z = [1, 2, 3, 4, 5]
print(z) # Output: [1, 2, 3, 4, 5]
print(type(z)) # Output: <class 'list'>

a = (1, 2, 3)
print(a) # Output: (1, 2, 3)
print(type(a)) # Output: <class 'tuple'>

b = {'name': 'John', 'age': 30}
print(b) # Output: {'name': 'John', 'age': 30}
print(type(b)) # Output: <class 'dict'>

# variables

>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.1415926535897931
>>> print(n)
17
>>> print(pi)
3.141592653589793

x = 5
x = 'string'
print(x)

name = "John"
age = 30
print("My name is " + name + " and I am " + str(age) + " years old.")

x = 5
y = 10
z = 15
print("The sum of x, y, and z is: " + str(x + y + z))
or
print("The sum of x, y, and z is:" , x + y + z)

fruits = ['apple', 'banana', 'orange', 'mango']
print("My third favorite fruit is " + fruits[2])

person = {'name': 'Jane', 'age': 25, 'city': 'New York'}
print("Jane is " + str(person['age']) + " years old.")

result = 3 * 4
print(result) # Output: 12

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(matrix)) # Output: <class 'list'>

coordinates = ((10, 20), (30, 40), (50, 60))
print(coordinates) # Output: ((10, 20), (30, 40), (50, 60))
print(type(coordinates)) # Output: <class 'tuple'>

employees = {'John': {'age': 30, 'position': 'Manager'},
             'Jane': {'age': 25, 'position': 'Developer'},
             'Bob': {'age': 35, 'position': 'CEO'}}
print(employees)
# Output: {'John': {'age': 30, 'position': 'Manager'},
#          'Jane': {'age': 25, 'position': 'Developer'},
#          'Bob': {'age': 35, 'position': 'CEO'}}
print(type(employees)) # Output: <class 'dict'>



# variable names and keywords

1_variable = 5 # invalid

variable name = "John" # invalid
variable@name = "John" # invalid

for = "loop" # invalid
if = True # invalid

myVariable = 5
print(myVariable) # Output: 5
myvariable = 10
print(myvariable) # Output: 10

_private_variable = 5 #not necessarily invalid but not recommended

Python reserves 35 keywords:

and del from None True
as elif global nonlocal try
assert else if not while
break except import or with
class False in pass yield
continue finally is raise async
def for lambda return await

# operators and operands

20+32
hour-1
hour*60+minute
minute/60
5**2
(5+9)*(15-7)

>>> minute = 59
>>> minute/60
0.9833333333333333

# modulus operator 

>>> quotient = 7 // 3
>>> print(quotient)
2

container_size = 100
item_size = 25
quotient = container_size // item_size
print(quotient) # Output: 4

>>> remainder = 7 % 3
>>> print(remainder)
1

x = 7
remainder = x % 2
if remainder == 0:
    print(x, "is even")
else:
    print(x, "is odd")

x = 123456
remainder = x % 10
print(remainder) # Output: 6

x = 10
y = 3
remainder = x % y
if remainder == 0:
    print(x, "is divisible by", y)
else:
    print(x, "is not divisible by", y)

# modulus operator

>>> first = 10
>>> second = 15
>>> print(first+second)
25

>>> first = '100'
>>> second = '150'
>>> print(first + second)
100150

>>> first = 'Test '
>>> second = 3
>>> print(first * second)
Test Test Test

# asking the user for input

>>> inp = input()
Some silly stuff
>>> print(inp)
Some silly stuff

>>> name = input('What is your name?\n')
What is your name?
Chuck
>>> print(name)
Chuck

prompt = 'Enter name:\n'
inp = input(prompt)

>>> int(speed)
17
>>> int(speed) + 5
22

# comments

# This is a single-line comment
x = 5 # This is also a single-line comment

'''
This is a
multi-line
comment
'''

def add(x, y):
    """
    This function takes two numbers as input and returns their sum.
    """
    return x + y

# exercises

Exercise 2: Write a program that uses input to prompt a user for their
name and then welcomes them.
Enter your name: Chuck
Hello Chuck


Exercise 3: Write a program to prompt the user for hours and rate per
hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
We wont worry about making sure our pay has exactly two digits after the decimal
place for now. If you want, you can play with the built-in Python round function
to properly round the resulting pay to two decimal places.


Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
converted temperature.

fahrenheit = celsius * 1.8 + 32
