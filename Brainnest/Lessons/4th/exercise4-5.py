def most_common_in_tuple(tuple):
    listify = list(tuple)
    return max(set(listify), key=listify.count)

print(most_common_in_tuple((1,2,2,3,4,5)))