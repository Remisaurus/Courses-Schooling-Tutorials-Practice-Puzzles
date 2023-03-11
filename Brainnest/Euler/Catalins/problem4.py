"""Define a function that takes a number as input and returns its word representation as a string,
without spaces or hyphens"""
def number_to_words(num):
    # Handle the special case of 1000 separately
    if num == 1000:
        return "onethousand"
    # Define lists for the words corresponding to the ones and tens places
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    # Initialize the word representation to an empty string
    words = ""
    # Handle the hundreds place if necessary
    if num >= 100:
        words += ones[num // 100] + "hundred"
        # Add "and" if the number has a non-zero ones or tens place
        if num % 100 != 0:
            words += "and"
    # Handle the ones and tens places
    if num % 100 < 20:
        words += ones[num % 100]
    else:
        words += tens[(num % 100) // 10] + ones[num % 10]
    # Return the word representation
    return words

# Initialize a variable to keep track of the total number of letters used
total_letters = 0
# Iterate over all the numbers from 1 to 1000 inclusive and add up the number of letters in their
# word representations
for num in range(1, 1001):
    total_letters += len(number_to_words(num))
    


# Print the total number of letters used
print("The total number of letters used is:", total_letters)