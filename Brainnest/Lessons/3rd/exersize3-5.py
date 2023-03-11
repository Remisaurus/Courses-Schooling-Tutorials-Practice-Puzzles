divisionals = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
start_at = 232000000 #previous attempts showed the number is higher than this.
not_finished = True
while not_finished:
    for each in divisionals:
        if start_at % each == 0:
            if each == 20:
                print(start_at)
                not_finished = False
                break
            else:
                continue
        else:
            start_at += 1
            break