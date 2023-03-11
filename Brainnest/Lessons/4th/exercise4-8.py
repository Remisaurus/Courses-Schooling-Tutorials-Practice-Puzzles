def get_even_numbers_from_tuple(tupler):
    return_list = []
    for every in tupler:
        try:
            number = int(every)
            if (number % 2) == 0:
                return_list.append(number)
        except:
            continue
    return_tuple = tuple(return_list)
    return return_tuple

print(get_even_numbers_from_tuple((1,2,3,4,5,6,7,8,9,'a','b')))