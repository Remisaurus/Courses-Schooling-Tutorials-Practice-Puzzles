# boolean expressions

x != y  # x is not equal to y
x > y  # x is greater than y
x < y  # x is less than y
x >= y  # x is greater than or equal to y
x <= y  # x is less than or equal to y
x is y  # x is the same as y
x is not y  # x is not the same as y

>>> 5 == 5
True
>>> 5 == 6
False

x = 5
y = 10
print(x < y) # Output: True

x = 5
y = "5"
print(x == int(y)) # Output: True

name1 = "John"
name2 = "Jane"
print(name1 != name2) # Output: True

fruits = ['apple', 'banana', 'orange']
print('banana' in fruits) # Output: True

person = {'name': 'John', 'age': 30}
print('age' in person) # Output: True

x = 5
print(isinstance(x, int)) # Output: True

x = 5
y = 10
z = 15
print((x < y) and (y < z)) # Output: True

>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>

# conditional execution 

if x > 0 :
	print('x is positive')

if x < 0 :
	pass
>>> x = 3
>>> if x < 10:
... print('Small')
...
Small
>>>

if x % 2 == 0 :
	print('x is even')
else :
	print('x is odd')

fruits = ['apple', 'banana', 'orange']
if 'banana' in fruits:
    print("banana is in the list")

person = {'name': 'John', 'age': 30}
if 'age' in person:
    print("age is a key in the dictionary")

x = 5
print("x is positive") if x > 0 else print("x is non-positive")

# chained conditionals

if x < y:
	print('x is less than y')
elif x > y:
	print('x is greater than y')
else:
	print('x and y are equal')

if choice == 'a':
	print('Bad guess')
elif choice == 'b':
	print('Good guess')
elif choice == 'c':
	print('Close, but not correct')

x = 5
y = 10

if x > 0 and y > 0:
    print("x and y are both positive")
elif x > 0 or y > 0:
    print("x or y is positive")
else:
    print("x and y are both non-positive")

# nested conditionals 

if x == y:
	print('x and y are equal')
else:
	if x < y:
		print('x is less than y')
	else:
		print('x is greater than y')

if 0 < x:
	if x < 10:
		print('x is a positive single-digit number.')

if 0 < x and x < 10:
	print('x is a positive single-digit number.')

# try and except

try:
  print(x)
except:
  print("An exception occurred") 

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong") 

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") 

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") 

# raise an exception

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") 

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed") 

age = 'five'
if not type(age) is int:
  raise TypeError("Only integers are allowed") 

x = 'name'
if type(x) == str:
  print("Your name is " + x)
elif x == int(x):
  print("Invalid!!!")

# exercises

Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program.

Exercise 3: Write a program to prompt for a score between 0.0 and
1.0. If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:

Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F