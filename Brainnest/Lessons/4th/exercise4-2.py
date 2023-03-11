import os

filename = input('filename (with extension):')

if filename == 'test.txt':
    print('No that file is not going to be opened.')
else:
    if os.path.isfile(f'./{filename}'):
        with open(filename, 'r') as input:
            for line in input:
                if line[-1] == '\n':
                    print(line[0:-1].upper())
                else:
                    print(line.upper())
    else:
        print('Filenotfound')
        raise FileNotFoundError
        