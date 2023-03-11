def main():
    heaviest_elf()
    print(top_three()[0] + top_three()[1] + top_three()[2])
    
    
    
def heaviest_elf():
    print(f'The elf carrying the most is elf {get_elftotal().index(max(get_elftotal())) + 1}. He carries: {max(get_elftotal())} calories.')

def top_three():
    top3 = []
    all = get_elftotal().copy()
    current = max(all)
    top3.append(current)
    all.remove(current)
    current = max(all)
    top3.append(current)
    all.remove(current)
    current = max(all)
    top3.append(current)
    all.remove(current)
    return top3
    
def get_elftotal():
    count = 0
    elftotal = []
    for line in get_data():
        if line != '\n':
            count += int(line)
            continue
        else:
            elftotal.append(count)
            count = 0
            continue
    return elftotal  

def get_data():
    input = []
    with open('input.txt', 'r') as boss:
        for line in boss:
            input.append(line)
        return input

main()