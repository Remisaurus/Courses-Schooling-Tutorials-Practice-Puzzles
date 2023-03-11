def palindrome_check(check_this):
    for each in range(0, len(str(check_this))):
        if str(check_this)[each] is str(check_this)[-each -1 ]:
            continue
        else:
            return False
    return True

def palindrome_in_tuple(tuple):
    list_of_palindrome_checks = []
    for every in tuple:
        list_of_palindrome_checks.append(palindrome_check(every))
    return list_of_palindrome_checks  

print(palindrome_in_tuple(('parterretrap', 'niet', 'treert', 'gezondheid')))
    
