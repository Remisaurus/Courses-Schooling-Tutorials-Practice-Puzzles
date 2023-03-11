import re

# Manually input input data (input1.txt)
# with current code it is neccesary to leave ample room for stacking
stack1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', 'F', 'V', 'Z', 'C', 'W', 'S', 'Q']
stack2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'R', 'Q']
stack3 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', 'M', 'P', 'Q', 'T', 'Z', 'B']
stack4 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'H', 'Q', 'R', 'F', 'V', 'D']
stack5 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', 'T', 'S', 'B', 'D', 'L', 'G', 'J']
stack6 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Z', 'T', 'R', 'W']
stack7 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'J', 'R', 'F', 'S', 'N', 'M', 'Q', 'H']
stack8 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'H', 'F', 'N', 'R']
stack9 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'R', 'P', 'Q', 'T', 'Z', 'J']

def main():
    input = retrieve_input('input2.txt')
    
    '''  
    part 1
    for every in input:
        current = extractnumbers(every)
        move_multiple_crates(current)  
    '''
    
    # part 2
    # Even though all seems to work correctly, the correct answer does not get produced. (this part fails).
    for every in input:
        current = extractnumbers(every)
        print(f'moving {current[0]} crates from {current[1]} (which has {crate_counter_precise(current[1])} crates) to {current[2]} (which has {crate_counter_precise(current[2])} crates).')
        new_crane(current)
        print(f'finished moving {current[0]} crates from {current[1]} (which now has {crate_counter_precise(current[1])} crates) to {current[2]} (which now has {crate_counter_precise(current[2])} crates).')
        
    '''
    print(stack8)
    print(stack9)
    new_crane([5,9,8])
    print(stack8)
    print(stack9)
    '''  
    '''
    print(stack1)
    print(stack2)
    print(stack3)
    print(stack4)
    print(stack5)
    print(stack6)
    print(stack7)
    print(stack8)
    print(stack9)
    '''
    print_top_crate(1)
    print_top_crate(2)
    print_top_crate(3)
    print_top_crate(4)
    print_top_crate(5)
    print_top_crate(6)
    print_top_crate(7)
    print_top_crate(8)
    print_top_crate(9)

def print_top_crate(stack):
    allcount = 0
    for all in globals()[f'stack{stack}']:
        if allcount == len(globals()[f'stack{stack}']):
            return ' '
        elif all == ' ':
            allcount += 1
            continue
        else:
            print(all)
            return all
        
def new_crane(three_numbers):
    amount_of_moves = three_numbers[0]
    while amount_of_moves > 0:
        available_chests = crate_counter(int(three_numbers[1]))
        if available_chests == 0:
            break
        elif amount_of_moves == 0:
            break
        elif available_chests == 1:
            move_single_crate(three_numbers)
            amount_of_moves -= 1
            continue      
        elif amount_of_moves == 1:
            move_single_crate(three_numbers)
            amount_of_moves -= 1
            continue      
        else:
            if amount_of_moves >= 3:
                amount_of_moves -= crate_counter(three_numbers[1])
                deploy_crate_stack(get_upto_crates(three_numbers[1], crate_counter(three_numbers[1])), three_numbers[2])
                continue
            if amount_of_moves == 2:
                deploy_crate_stack(get_upto_crates(three_numbers[1], 2), three_numbers[2])
                amount_of_moves -= 2
                continue

def get_upto_crates(fromstack, number):
    count = 0
    ff = []
    allcount = 0
    for all in globals()[f'stack{fromstack}']:
        if count >= number:
            break
        if allcount >= len(globals()[f'stack{fromstack}']):
            ff.append(globals()[f'stack{fromstack}'][allcount])
            globals()[f'stack{fromstack}'][allcount] = ' '
            count += 1
            allcount += 1
            break
        elif all == ' ':
            allcount += 1
            continue
        else:
            ff.append(globals()[f'stack{fromstack}'][allcount])
            globals()[f'stack{fromstack}'][allcount] = ' '
            allcount += 1
            count += 1
            continue
    return ff

def crate_counter_precise(stack):
    count = 0
    for all in globals()[f'stack{stack}']:
        if all != ' ':
            count += 1
    return count
        
def crate_counter(stack):
    if globals()[f'stack{stack}'][-1] == ' ':
        return 0
    elif globals()[f'stack{stack}'][-2] == ' ':
        return 1
    elif globals()[f'stack{stack}'][-3] == ' ':
        return 2
    else:
        return 3 
    # counts if there are 3+ crates or less left.    
    
def deploy_crate_stack(list, tostack):
    count = -1
    for all in list:
        allcount = 0
        for all in globals()[f'stack{int(tostack)}']:
            if allcount + 1 >= len(globals()[f'stack{int(tostack)}']):
                if globals()[f'stack{int(tostack)}'][allcount] != ' ':
                    globals()[f'stack{int(tostack)}'][allcount - 1] = list[count]
                    count -= 1
                    break
                else:
                    globals()[f'stack{int(tostack)}'][allcount] = list[count]
                    count -= 1
                    break
            elif all == ' ':
                allcount += 1
                continue
            else:
                globals()[f'stack{int(tostack)}'][allcount - 1] = list[count]
                count -= 1
                break
    

def move_multiple_crates(three_numbers): #crane with one move at a time
    move_number = 1
    while move_number <= int(three_numbers[0]):
        move_single_crate(three_numbers)
        move_number += 1
    
def move_single_crate(three_numbers):
    gotten_crate = get_single_crate(int(three_numbers[1])) 
    if gotten_crate != ' ' and gotten_crate is not None:
        deploy_single_crate(gotten_crate, int(three_numbers[2]))
 
def get_single_crate(fromstack):
    allcount = 0
    ff = ' '
    for all in globals()[f'stack{fromstack}']:
        if allcount >= len(globals()[f'stack{fromstack}']):
            ff = globals()[f'stack{fromstack}'][allcount]
            globals()[f'stack{fromstack}'][allcount] = ' '
            return ff
        elif all == ' ':
            allcount += 1
            continue
        else:
            ff = globals()[f'stack{fromstack}'][allcount]
            globals()[f'stack{fromstack}'][allcount] = ' '
            return ff

def deploy_single_crate(crate, tostack):
    allcount = 0
    for all in globals()[f'stack{int(tostack)}']:
        if allcount + 1 >= len(globals()[f'stack{int(tostack)}']):
            if globals()[f'stack{int(tostack)}'][allcount] != ' ':
                globals()[f'stack{int(tostack)}'][allcount - 1] = crate 
                break
            else:
                globals()[f'stack{int(tostack)}'][allcount] = crate
                break
        elif all == ' ':
            allcount += 1
            continue
        else:
            globals()[f'stack{int(tostack)}'][allcount - 1] = crate
            break
    
def extractnumbers(line):
    numbers = []
    numberreg = '[0-9]*'
    for all in re.findall(numberreg, line):
        if all == '':
            continue
        numbers.append(int(all))
    return numbers
       
def retrieve_input(inputfile):
    input_list = []
    with open (inputfile, 'r') as input:
        for line in input:
            input_list.append(line)
    return input_list

if __name__ == '__main__':
    main()