def main():
    input = fetch_input()
    # part 1
    number = 0
    for all in input:
        fournumbers = disect(all)
        make_map = make_number_list(fournumbers)
        fit = check_if_fits_completely(make_map)
        if fit is True:
            number += 1
        else:
            continue
    print(f'a complete fit is noticed in {number} cases')
    # part 2
    number = 0
    for all in input:
        fournumbers = disect(all)
        make_map = make_number_list(fournumbers)
        fit = check_if_overlaps(make_map)
        if fit is True:
            number += 1
        else:
            continue
    print(f'overlap noticed in {number} cases')
        

def check_if_overlaps(twolists):
    for every in twolists[0]:
        if every in twolists[1]:
            return True
        else:
            continue
    return False

def check_if_fits_completely(twolists): #checks if one of the two lists fits completely in the other
    fitsone = True
    fitstwo = True
    for all in twolists[0]:
        if all in twolists[1]:
            continue
        else:
            fitsone = False
            break
    for all in twolists[1]:
        if all in twolists[0]:
            continue
        else:
            fitstwo = False
            break
    if fitsone is True:
        return True
    if fitstwo is True:
        return True
    else:
        return False 

def make_number_list(fournumbers): # makes list of two lists out of the four number extracted
    list1 = []
    list2 = []
    both = []
    count = 0 
    while fournumbers[0] + count <= fournumbers[1]:
        list1.append(fournumbers[0]+count)
        count +=1
    both.append(list1)
    count = 0
    while fournumbers[2] + count <= fournumbers[3]:
        list2.append(fournumbers[2]+count)
        count +=1
    both.append(list2)
    return both
   
def disect(string): # to get the important numbers
    current_list = [*string + ' ']
    current_number = 1
    number = 0
    extracted_numbers = []
    for all in current_list:
        if all == '-':
            extracted_numbers.append(int(number * current_number))
            current_number = 1
            number = 0
            continue
        elif all == ',':
            extracted_numbers.append(int(number * current_number))
            current_number = 1
            number = 0
            continue
        elif all == ' ':
            extracted_numbers.append(int(number * current_number))
            current_number = 1
            number = 0
            break
        elif all == '\n':
            extracted_numbers.append(int(number * current_number))
            current_number = 1
            number = 0
            break
        else:
            if current_number == 1 and number == 0:
                number = int(all)
                continue
            elif current_number == 1 and number != 0:
                number += (0.1 * int(all))
                current_number = 10
                continue
            elif current_number == 10:
                number += (0.01 * int(all))
                current_number = 100
                continue
            else:
                print('requires more code for numbers of 1000 and higher')
    return extracted_numbers

def fetch_input():
    inputlist = []
    with open('input.txt', 'r') as input:
        for all in input:
            inputlist.append(all)
    return inputlist

main()