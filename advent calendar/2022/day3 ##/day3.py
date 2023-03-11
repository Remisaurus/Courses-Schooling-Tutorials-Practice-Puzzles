scoringstring = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    List_of_input = fetch_input()
    list_of_groups = create_groups()
    # part 1
    total = 0
    for each in List_of_input:
        total += score_single(check_double(half_this(each)))
    print(total)
    # part 2
    part2total = 0
    for each in find_badge():
        part2total += score_single(each)
    print(part2total)
        

def find_badge():
    badge_list= []
    for all in create_groups():
        for every in all[0]:
            if every == '\n':
                continue
            if every in all[1] and every in all[2]:
                badge_list.append(every)
                break
    return badge_list
                
def create_groups():
    group = 1
    member = 1
    List_of_input = fetch_input()
    grouplist = []
    globals()[f'group{group}'] = []
    for everyone in List_of_input:
        globals()[f'group{group}'].append(everyone)
        member += 1
        if member > 3:
            grouplist.append(globals()[f'group{group}'])
            group += 1 
            globals()[f'group{group}'] = []
            member = 1
    return grouplist
        
def score_single(letter):
    return scoringstring.index(letter)

def check_double(twohalves):
    for every in twohalves[0]:
        if every in twohalves[1]:
            return every
    print('no doubles noticed')

def half_this(string):
    indexmax = 0
    halves = []
    for each in string:
        indexmax +=1
    indexhalf = int(0.5 * indexmax)
    halves.append(string[:indexhalf])
    halves.append(string[indexhalf:])
    return halves        

def fetch_input():
    inputlist = []
    with open ('input.txt', 'r') as input:
        for each in input:
            inputlist.append(each)
    return inputlist

main()