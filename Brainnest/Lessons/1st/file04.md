# exercise

import sys

def collatz(number):
    if number == 'done':
        sys.exit()
    elif int(number) % 2 == 0:
        print(int(number) // 2)
    else:
        print(3 * int(number) + 1)

while True:
    collatz(input("Enter a number:\n> "))
    print("Type 'done' to exit.")


# exercise

# problem
print('Good morning!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good afternoon!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good evening!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')

# solution 1
def askFeeling():
 print('How are you feeling?')
 feeling = input()
 print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good morning!')
askFeeling()
print('Good afternoon!')
askFeeling()
print('Good evening!')
askFeeling()

# solution 2
for timeOfDay in ['morning', 'afternoon', 'evening']:
 print('Good ' + timeOfDay + '!')
 print('How are you feeling?')
 feeling = input()
 print('I am happy to hear that you are feeling ' + feeling + '.')

# solution 3
def askFeeling(timeOfDay):
 print('Good ' + timeOfDay + '!')
 print('How are you feeling?')
 feeling = input()
 print('I am happy to hear that you are feeling ' + feeling + '.')
for timeOfDay in ['morning', 'afternoon', 'evening']:
 askFeeling(timeOfDay)

# while loop

x = 0
x = x + 1
print(x)

n = 5
while n > 0:
	print(n)
	n = n - 1
print('Finished!')

while True:
	line = input('> ')
	if line == 'done':
		break
	print(line)
print('Done!')

i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

spam = 0
while spam < 5:
	print('Hello, world.')
	spam = spam + 1

name = ''
while name != 'your name':
	print('Please type your name.')
	name = input()
print('Thank you!')

while True:
	print('Please type your name.')
	name = input()
	if name == 'your name':
		break
print('Thank you!')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

# for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

print('My name is')
for i in range(5):
  print('Jimmy')

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
	print('Happy New Year:', friend)
print('Done!')

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
	count = count + 1
print('Count: ', count)

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
	total = total + itervar
print('Total: ', total)


# exercises

Exercise 1: Write a program which repeatedly reads numbers until the
user enters `done`. Once `done` is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333

Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.

