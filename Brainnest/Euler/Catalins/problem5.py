# Define a function that takes a year and a month and returns the number of days in that month
def days_in_month(year, month):
    if month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 31


# Initialize a variable to keep track of the number of Sundays that fell on the first of the month
sundays_on_first = 0
# Initialize a variable to keep track of the day of the week (0 = Monday, 1 = Tuesday, etc.)
day_of_week = 1  # 1 Jan 1900 was a Monday
# Iterate over all the years from 1900 to 2000 inclusive
for year in range(1900, 2001):
    # Iterate over all the months from 1 to 12 inclusive
    for month in range(1, 13):
        # If the year is greater than 1900 and the day of the week is 0 (i.e., Sunday), increment the
        # counter of Sundays on the first of the month
        if year > 1900 and day_of_week == 0:
            sundays_on_first += 1
        # Compute the number of days in the current month and update the day of the week accordingly
        days = days_in_month(year, month)
        day_of_week = (day_of_week + days) % 7
# Print the result
print("The number of Sundays that fell on the first of the month during the twentieth century is:", sundays_on_first)
