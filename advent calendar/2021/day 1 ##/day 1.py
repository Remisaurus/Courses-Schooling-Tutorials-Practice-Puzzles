def main():
    # print(plus_counter(fetch_input())) # solves part 1
    print(plus_counter(make_new_list(fetch_input())))
    #cprint(make_new_list(fetch_input()))


def make_new_list(list):
    new_data = []
    counter = 0
    for all in list:
        if counter == 0:
            counter += 1
            continue
        try:
            new_data.append(int(list[counter]) + int(list[counter - 1]) + int(list[counter + 1]))
            counter += 1
        except IndexError:
            new_data.append(0)
            counter += 1   
    return new_data

def plus_counter(list):
    counter = 0
    plusses = 0
    for all in list:
        if counter == 0:
            counter += 1
            continue
        elif plus_or_not(int(list[counter]), int(list[counter - 1])):
            plusses += 1
            counter += 1
        else:
            counter += 1
    return plusses

def plus_or_not(one, two):
    if one - two > 0:
        return True
    else:
        return False

def fetch_input():
    input_list = []
    with open ('input.txt', 'r') as input:
        for line in input:
            input_list.append(line)
    return input_list

if __name__ == '__main__':
    main()
    