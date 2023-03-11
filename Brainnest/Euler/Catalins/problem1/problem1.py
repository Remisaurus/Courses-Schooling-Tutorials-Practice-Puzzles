with open("numbers.txt", "r") as numbers:
    num_list = [int(line.strip()) for line in numbers]

total_sum = sum(num_list)
first_ten_digits_of_the_sum = str(total_sum)[:10]

# Print the first ten digits of the sum
print("The first ten digits of the sum are:", first_ten_digits_of_the_sum)