import re
def main():
    #part1
    #print(multiple_moves(dissect_input()))
    #print(multiple_moves(dissect_input())[0] * multiple_moves(dissect_input())[1])
    print(multiple_moves_part2(dissect_input()))
    print(multiple_moves_part2(dissect_input())[0] * multiple_moves_part2(dissect_input())[1])


def multiple_moves_part2(list):
    depth = 0
    horizontal = 0
    aim = 0
    for orders in list:
        if orders[1] == 'f':
            horizontal += int(orders[0])
            depth += int(orders[0]) * aim
        elif orders[1] == 'd':
            aim += int(orders[0])
        elif orders[1] == 'u':
            aim -= int(orders[0])
    return [depth, horizontal, aim]
    
    
def multiple_moves(list):
    depth = 0
    horizontal = 0 
    for all in list:
        depth += move(all)[0]
        horizontal += move(all)[1]
    return [depth, horizontal]
    
def move(orders):
    depth = 0
    horizontal = 0
    if orders[1] == 'f':
        horizontal += int(orders[0])
    elif orders[1] == 'd':
        depth += int(orders[0])
    elif orders[1] == 'u':
        depth -= int(orders[0])
    return [depth, horizontal]
    
def dissect_input():
    total = []
    numberreg = r'\d\d*'
    letterreg = r'\D'
    for each in fetch_input():
        current = []
        current.append(re.search(numberreg, each).group())
        current.append(re.search(letterreg, each).group())
        total.append(current)
    return total   

def fetch_input():
    input_list = []
    with open ('input.txt', 'r') as input:
        for line in input:
            input_list.append(line)
    return input_list

if __name__ == '__main__':
    main()