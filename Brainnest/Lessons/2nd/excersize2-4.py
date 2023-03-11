christmas = True
count = 0
total = 0

while christmas:
    print('enter a integer number please:')
    last_input = input()
    try:
        number = int(last_input)
    except ValueError:
        if last_input == 'done':
            try:
                print(f'{total} {count} {total / count}')
            except ZeroDivisionError:
                print('You have not input a single number.')
            quit()
        else:
            print('please enter an integer number or write done (no caps) when finished.')
            continue
    total += number
    count += 1
    

        