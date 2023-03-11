def find_unique_in_tuple(tupler):
    return_list = []
    for each in tupler:
        if each not in return_list:
            return_list.append(each)
    return_tuple = tuple(return_list)
    return return_tuple

print(find_unique_in_tuple((1,2,3,4,4,4,5,5,6,6,6,6,7,7,7,8,8,9,0)))