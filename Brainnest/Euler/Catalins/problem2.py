from datetime import datetime


# Function to calculate the next number in the sequence
def get_next_in_sequence(curr_no):
    if curr_no % 2 == 0:  # If current number is even
        return curr_no / 2
    else:
        return curr_no * 3 + 1  # Multiply current number by 3 and add 1


# Function to get the number of items in the sequence for a given number
def get_no_of_items(no, already_known_no):
    count = 1  # Initialize count to 1
    curr_no = no  # Set current number to input number
    while curr_no != 1:  # Loop until current number is 1
        if curr_no in already_known_no:  # If current number is already in dictionary of known numbers
            count += already_known_no[curr_no] - 1  # Increment count by value of known number minus 1
            break
        else:
            count += 1  # Increment count by 1
            curr_no = get_next_in_sequence(curr_no)  # Calculate next number in sequence
    return count


# Main function to find the number with the longest sequence within a given limit
def main(limit):
    start = datetime.now()  # Record start time
    curr_highest = 0  # Initialize current highest count to 0
    already_known_no = {}  # Create an empty dictionary to store known numbers and their sequence lengths
    # I think this dict is the most valuable part of the code, because without it, code runs in way higher time O(n)

    for no in range(1, limit):  # Loop through numbers from 1 to limit
        curr_no_count = get_no_of_items(no,
                                        already_known_no)  # Get the number of items in the seq for the curr_no
        already_known_no[no] = curr_no_count
        curr_highest = curr_no_count if curr_no_count > curr_highest else curr_highest
        # Update the current highest count if the current count is higher

    finish = datetime.now()  # Record finish time

    print(curr_highest)  # Print the highest count
    print(f"total time elapsed {finish - start}")  # Print the time elapsed


main(1000000)
