'''
1. Sort a list of dictionaries: Write a lambda function,
that sorts a list of dictionaries by a specified key.
For example, given the list of dictionaries 
[{ 'name': 'John', 'age': 25 }, { 'name': 'Alice', 'age': 30 },
{ 'name': 'Bob', 'age': 20 }],
the lambda function should sort the list by age and return
[{ 'name': 'Bob', 'age': 20 },
{ 'name': 'John', 'age': 25 }, { 'name': 'Alice', 'age': 30 }].
'''
li = [{ 'name': 'John', 'age': 25 }, { 'name': 'Alice', 'age': 30 }, { 'name': 'Bob', 'age': 20 }]

print(sorted(li, key=lambda i: i['age']))

'''
2. 
Calculate the average: Write a lambda function that takes a list of numbers as input
and returns the average value.
For example, given the list [1, 2, 3, 4, 5],
the lambda function should return 3.
'''
li = [1, 2, 3, 4, 5]

result = lambda x: sum(x) / len(x)

print(result(li))

'''
3.
Find the largest number:
Write a lambda function that takes a list of numbers as input and returns the largest number in the list.
For example, given the list [1, 5, 3, 9, 2], the lambda function should return 9.
'''

li = [1, 5, 3, 9, 2]

print(max(li, key=lambda x: int(x)))

'''
4.
Flatten a nested list:
Write a lambda function that takes a nested list as input and returns a flattened list.
For example, given the nested list [1, [2, [3, 4], 5], 6],
the lambda function should return [1, 2, 3, 4, 5, 6].
'''

#


'''
5. Calculate the median:
Write a lambda function that takes a list of numbers as input and returns the median value.
If the list has an even number of elements,
the median should be the average of the middle two elements. For example,
given the list [1, 2, 3, 4, 5, 6], the lambda function should return 3.5.
'''

#
from statistics import median

li=[1, 2, 3, 4, 5, 6]

me=lambda li:median(li)
result=me(li)

print(result)
