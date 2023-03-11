# import re

# txt = 'The rain in Spain'
# x = re.findall('ai', txt)
# y = re.search('ai', txt)


# print(x, y)

'''
Write a regular expression that matches a date in the format dd/mm/yyyy.
For example, the string "01/01/2021" should match.
'''

import re
date = re.compile("^\d{2}/{1}\d{2}/{1}\d{4}$")
print(date.search( "12/12/1222" ))

'''
2. Write a regular expression that matches a phone number in the format xxx-xxx-xxxx,
where x is a digit. For example, the string "123-456-7890" should match.
'''

phone = re.compile("^\d{3}\-{1}\d{3}\-{1}\d{4}$")
print(phone.search( "123-456-7890" ))

'''
3. Write a regular expression that matches a string that starts with a word,
followed by one or more whitespace characters,
followed by another word. For example,
the string "hello world" should match.
'''

twowords = re.compile("\w+\s+\w+")
print(twowords.search("hello world"))

'''
final. Write a regular expression that matches a string that contains a number with exactly two decimal places.
For example, the string "1.23" should match,
but the string "1.234" should not match.
'''


twodecimals = re.compile(r"\d+.{1}\d{2}\b")
print(twodecimals.search("1.23"))
print(twodecimals.search("1.234"))