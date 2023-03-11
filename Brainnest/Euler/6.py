'''n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!'''

def digits(n): # makes resulting number from n!
    number_list = []
    for each in range (1, n):
        number_list.append(each)
    result = 0
    for every in number_list:
        if result == 0:
            result += every * n
        else:
            result += result * every
    return result

def sum_of_digits(number): # makes a string of a number and breaks it into 1 digit lengths. these are all added and returned
    string = str(number)
    all_digits = [*string]
    result = 0
    for every in all_digits:
        result += int(every)
    return result

print(sum_of_digits(digits(100)))

