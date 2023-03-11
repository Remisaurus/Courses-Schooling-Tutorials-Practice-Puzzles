def palindrome_check(check_this):
    for each in range(0, len(str(check_this))):
        if str(check_this)[each] is str(check_this)[-each -1 ]:
            continue
        else:
            return False
    return True

def create_three_digit_list():
    created_list = []
    for each in range(999, 99, -1):
        created_list.append(each)
    return created_list

three_digit_list = create_three_digit_list()

all_possibilities = []

for each in three_digit_list:
    for every in three_digit_list:
        all_possibilities.append(each * every)
        
palindromes_in_possibilities = []
        
for each in all_possibilities:
    if palindrome_check(each):
        palindromes_in_possibilities.append(each)
        
print(max(palindromes_in_possibilities))
        