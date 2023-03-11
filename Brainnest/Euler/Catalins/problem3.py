two_to_the_power_of_1000_str = str(pow(2, 1000))  # Raise 2 to the power of 1000 and convert it to str
running_sum = 0
for no in two_to_the_power_of_1000_str:  # go through each digit in the number and add it to the running_sum
    running_sum += int(no)

print(running_sum)
