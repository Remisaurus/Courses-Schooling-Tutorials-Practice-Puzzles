def main():
    input = fetch_input()
    '''
    part1
    
    print(calculate_from_mostleast_binary_list(make_mostleast_list(input)))
    print(check_calculation(make_mostleast_list(input)))
    results = calculate_from_mostleast_binary_list(make_mostleast_list(input))
    print(results[0] * results[1])
    '''
    # part 2
    
    # even though logic seems sound and seems to function correctly, the answer does not satisfy.
    print(get_last_one(input)) 
    primary = binary_string_converter(get_last_one(input)[0])
  
    print(get_last_zero(input))
    secondary = binary_string_converter(get_last_zero(input)[0])
    
    print(primary, secondary, primary * secondary)
    
def binary_string_converter(string):
    inverse = string[11::-1]
    binarycount = 0
    number = 0
    for each in inverse:
        if binarycount == 0:
            number += int(each)
            binarycount += 1
            continue
        number += (2 * int(each)) ** (binarycount)
        binarycount += 1
    return number
    
def get_last_one(list):
    listcopy = list.copy()
    counter = 0
    while len(listcopy) > 1:
        if check_most_one(listcopy, counter) is None:
            print('nonalert')
            counter = 0
            continue
        elif check_most_one(listcopy, counter) == 1:
            for each in list:
                if int(each[counter]) == 0:
                    try:
                        listcopy.remove(each)
                    except (IndexError, ValueError):
                        continue
        elif check_most_one(listcopy, counter) == 0:
            for each in list:
                if int(each[counter]) == 1:
                    try:
                        listcopy.remove(each)
                    except (IndexError, ValueError):
                        continue
        counter += 1
    return listcopy
        
def get_last_zero(list):
    listcopy = list.copy()
    counter = 0
    while len(listcopy) > 1:
        if check_most_zero(listcopy, counter) is None:
            counter = 0
            print('nonalert')
            continue
        elif check_most_zero(listcopy, counter) == 1:
            for each in list:
                try:
                    if int(each[counter]) == 0:
                        listcopy.remove(each)
                except (IndexError, ValueError ):
                    continue
        elif check_most_zero(listcopy, counter) == 0:
            for each in list:
                try:
                    if int(each[counter]) == 1:
                        listcopy.remove(each)
                except (IndexError, ValueError ):
                    continue
        counter += 1
    return listcopy     
    
def check_calculation(list):
    most = 1*list[0][0] + 2*list[1][0] + 4*list[2][0] + 8*list[3][0] + 16*list[4][0] + 32*list[5][0] + 64*list[6][0] + 128*list[7][0] + 256*list[8][0] + 512*list[9][0] + 1024*list[10][0] + 2048*list[11][0] 
    least = 1*list[0][1] + 2*list[1][1] + 4*list[2][1] + 8*list[3][1] + 16*list[4][1] + 32*list[5][1] + 64*list[6][1] + 128*list[7][1] + 256*list[8][1] + 512*list[9][1] + 1024*list[10][1] + 2048*list[11][1]
    return [most, least]
    
def calculate_from_mostleast_binary_list(list):
    binarycount = 0
    most = 0
    least = 0
    for each in list:
        if binarycount == 0:
            most += each[0]
            least += each[1]
            binarycount += 1
            continue
        most += (2 * each[0]) ** binarycount
        least += (2 * each[1]) ** binarycount
        binarycount += 1
    return [most, least]

def make_mostleast_list(inputlist):
    mostleast = []
    count = 0
    for every in inputlist[0]:
        mostleast.insert(0, check_most(inputlist, count))
        count += 1
    for each in mostleast:
        if each == None:
            mostleast.remove(None)
    return mostleast

def check_most(inputlist, index):
    ones = 0
    zeros = 0
    for all in inputlist:
        try:
            if int(all[index]) == 1:
                ones += 1
            if int(all[index]) == 0:
                zeros += 1
        except (ValueError, IndexError):
            continue
    if zeros == ones:
        print (zeros, ones, 'equality alert!')
    if zeros > ones:
        return [0 , 1]
    if ones > zeros:
        return [1 , 0]
    
def check_most_one(inputlist, index):
    ones = 0
    zeros = 0
    for all in inputlist:
        try:
            if all[index] == '1':
                ones += 1
            if all[index] == '0':
                zeros += 1
        except (ValueError, IndexError):
            continue
    if zeros == 0 and ones == 0:
        return None
    if zeros > ones:
        return 0
    if ones >= zeros:
        return 1
    
def check_most_zero(inputlist, index):
    ones = 0
    zeros = 0
    for all in inputlist:
        try:
            if all[index] == '1':
                ones += 1
            if all[index] == '0':
                zeros += 1
        except (ValueError, IndexError):
            continue
    if zeros == 0 and ones == 0:
        return None
    if zeros >= ones:
        return 0
    if ones > zeros:
        return 1

def fetch_input():
    input_list = []
    with open ('input.txt', 'r') as input:
        for line in input:
            input_list.append(line)
    return input_list

if __name__ == '__main__':
    main()
    