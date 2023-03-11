def get_frequency_in_tuple(tuple):
    frequency_dict = {}
    for item in tuple:
        if item not in frequency_dict:
            frequency_dict[item] = 1
        else:
            frequency_dict[item] += 1
    return frequency_dict      
        
print(get_frequency_in_tuple((1,2,3,4,5,6,6,7,7,7,8,8,8,8)))
    