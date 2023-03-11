try:
    grade = float(input("grade: "))
except ValueError:
    print('unrecognized number')
    quit()

if 1.0 >= grade >= 0.9:
    print('A')
elif 0.9 > grade >= 0.8:
    print('B')
elif 0.8 > grade >= 0.7:
    print('C')
elif 0.7 > grade >= 0.6:
    print('D')
elif 0.6 > grade >= 0.0:
    print('F')
else:
    print('Give a grade value between 0 and 1 please')
    raise Exception('out of range')

