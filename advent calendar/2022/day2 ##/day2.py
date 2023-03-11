def main():
    # print(all_score())
    print(all_score2())
'''
rock paper scissors [1] x y z , [0] a b c 
'''

def all_score2():
    total = 0
    counter = 0
    for each in retrieve_input():
        total += score2(current(counter))
        counter += 1
        continue
    return total  

def score2(info):
    if info[1] == 'X':
        if info[0] == 'A':
            return 3
        elif info[0] == 'B':
            return 1
        elif info[0] == 'C':
            return 2
        else:
            print('something is wrong here')
    if info[1] == 'Y':
        if info[0] == 'A':
            return 4
        elif info[0] == 'B':
            return 5
        elif info[0] == 'C':
            return 6
        else:
            print('something is wrong here')
    if info[1] == 'Z':
        if info[0] == 'A':
            return 8
        elif info[0] == 'B':
            return 9
        elif info[0] == 'C':
            return 7
        else:
            print('something is wrong here')   

def all_score():
    total = 0
    counter = 0
    for each in retrieve_input():
        total += score(current(counter))
        counter += 1
        continue
    return total  

def score(info):
    if info[1] == 'X':
        score = 1
        if info[0] == 'A':
            score += 3 
            return score
        elif info[0] == 'B':
            return score
        elif info[0] == 'C':
            score += 6
            return score
        else:
            print('something is wrong here')
    if info[1] == 'Y':
        score = 2
        if info[0] == 'A':
            score += 6
            return score
        elif info[0] == 'B':
            score += 3
            return score
        elif info[0] == 'C':
            return score
        else:
            print('something is wrong here')
    if info[1] == 'Z':
        score = 3 
        if info[0] == 'A':
            return score
        elif info[0] == 'B':
            score += 6
            return score
        elif info[0] == 'C':
            score += 3
            return score
        else:
            print('something is wrong here')
    

def current(index):
    currenttwo = []
    currenttwo.append(retrieve_input()[index][0])
    currenttwo.append(retrieve_input()[index][2])
    return currenttwo

def retrieve_input():
    input_list = []
    with open ('input.txt', 'r') as input:
        for line in input:
            input_list.append(line)
    return input_list

main()      
        
        
    