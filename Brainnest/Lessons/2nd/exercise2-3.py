def feely():
    time_of_day = ['morning', 'afternoon', 'evening']
    for each in time_of_day:
        print('Good ' + each + '.')
        print('How are you feeling?')
        feeling = input()
        print('I am happy to hear that you are feeling ' + feeling + '.')

feely()
