def three_and_five(number_to_check):
    '''
    this function works BELOW the number to check so does not include it.
    '''
    total_in_three = []
    total_in_five = []
    total = 0
    for each in range(0, number_to_check, 3):
        total_in_three.append(each)
    for each in range(0, number_to_check, 5):
        total_in_five.append(each)
    for each in total_in_three:
        total += each
    for each in total_in_five:
        if each not in total_in_three:
            total += each
        
    print(total)
    return total

three_and_five(1000)