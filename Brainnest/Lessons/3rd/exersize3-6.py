n = 100

list_of_n = []
for each in range (1 , n+1):
    list_of_n.append(each)

sum_of_squares = 0
for each in list_of_n:
    sum_of_squares += each ** 2
    
square_of_sums = 0
for each in list_of_n:
    square_of_sums += each
square_of_sums = square_of_sums ** 2
    
print(sum_of_squares)    
print(square_of_sums)
print(f'the difference is: {square_of_sums - sum_of_squares}')
