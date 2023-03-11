# this is for part one of the advent puzzle. part two is currently not made yet.

def main():
    global current_row
    global current_direction
    global current_column
    current_row = 1 # starting on row 1
    current_column = get_starting_column()
    current_direction = 0 # 0 = R, 1 = Down, 2 = Left, 3 = Up
    
    for all in chop_code():
        if all == 'R':
            turn('R') 
            continue
        if all == 'L':
            turn('L') 
            continue
        else:
            move(int(all))
    print(current_row)
    print(current_column)
    print(current_direction)

def turn(LR):
    global current_direction
    if LR == 'L':
        current_direction -= 1
        if current_direction == -1:
            current_direction = 3
    elif LR == 'R':
        current_direction += 1
        if current_direction == 4:
            current_direction = 0
    
def move(steps):
    global current_direction
    global current_column
    global current_row
    count = 0 
    if current_direction == 0: # To the right
        walkway = ' ' + get_map()[current_row] + ' '
        while steps > 0:
            if walkway[current_column + 1] == '.':
                steps -= 1
                current_column += 1
                continue
            elif walkway[current_column + 1] == '#':
                steps -= 100
                continue
            elif walkway[current_column + 1].isspace():
                for all in walkway: 
                    if all != ' ':
                        if all == '#':
                            steps -= 100
                            break
                        if all == '.':
                            steps -= 1
                            current_column = walkway.find('.')
                            break
                continue
    if current_direction == 2: # To the Left
        walkway = ' ' + get_map()[current_row] + ' '
        while steps > 0:
            if walkway[current_column - 1] == '.':
                steps -= 1
                current_column -= 1
                continue
            elif walkway[current_column - 1] == '#':
                steps -= 100
                continue
            elif walkway[current_column - 1].isspace():
                inverted_walkway = walkway[::-1]
                for all in inverted_walkway: 
                    if all != ' ':
                        if all == '#':
                            steps -= 10000
                            break
                        if all == '.':
                            steps -= 1
                            def check_steps_to_right(string):
                                number = -1 
                                for all in string:
                                    if all != ' ':
                                        number += 1
                                        continue
                                return number
                            current_column += check_steps_to_right(walkway)
                            break
                continue
    if current_direction == 1: # Downwards
        walk_column = current_column - 1
        while steps > 0:
            next_row = current_row + 1
            if get_map()[next_row][walk_column] == '.':
                steps -= 1
                current_row += 1
                continue
            elif get_map()[next_row][walk_column] == '#':
                steps -= 100
                continue
            elif get_map()[next_row][walk_column].isspace():
                for row in get_map():
                    if row[walk_column].isspace():
                        count += 1
                        continue
                    elif row[walk_column] == '.':
                        steps -= 1 
                        current_row = count
                        break
                    elif row[walk_column] == '#':
                        steps -= 10000
                        break
                continue
    if current_direction == 3: # upwards
        walk_column = current_column - 1
        while steps > 0:
            next_row = current_row - 1
            if get_map()[next_row][walk_column] == '.':
                steps -= 1
                current_row -= 1
                continue
            elif get_map()[next_row][walk_column] == '#':
                steps -= 100
                continue
            elif get_map()[next_row][walk_column].isspace():
                searchback = []
                for row in get_map():
                    searchback.append(row[walk_column])
                searchbackstring = ''.join(searchback)
                searchbackstringrev = searchbackstring[::-1]
                for all in searchbackstringrev:
                    if all != ' ':
                        if all == '#':
                            steps -= 10000
                            break
                        if all == '.':
                            steps -= 1
                            def check_steps_downwards(string):
                                number = -1 
                                for all in string:
                                    if all != ' ':
                                        number += 1
                                        continue
                                return number
                            current_row += check_steps_downwards(searchbackstring)
                            break
                continue
                    
def get_map(): # list of map with row number being index. (row 0 is empty) 
    with open('inputmap.txt', 'r') as boss:
        maplist = [1001 * ' ']
        for line in boss:
            maplist.append(line)
        maplist.append(1001 * ' ')
        return maplist

def get_starting_column(): # facing to the right on row 1 and column as stated by this function
    count = 1
    for all in get_map()[1]:
        if all != '.':
            count += 1
            continue
        else:
            return count

def get_code():
    with open('inputcode.txt', 'r') as boss:
        code = ''
        for line in boss:
            code = line
        return code
    
def chop_code():
    count = 0
    chopped_code = []
    skip_one = False
    for all in get_code():
        if skip_one == True:
            skip_one = False
            count += 1
            continue
        if all == 'L':
            chopped_code.append('L')
            count += 1
            continue
        elif all == 'R':
            chopped_code.append('R')
            count += 1
            continue
        else:
            if get_code()[count+1] == 'R' or get_code()[count+1] == 'L':
                chopped_code.append(all)
                count += 1
                continue
            else:
                this = all + get_code()[count+1]
                skip_one = True
                chopped_code.append(this)
                count += 1
                continue
    return chopped_code 

main()          
         