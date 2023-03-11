# only works with diagonal lines or hori/verti lines that are incrementing.
# Every point where crossing happens at least once

ventlist= []
ventlist.append('0,9 -> 5,9')
ventlist.append('8,0 -> 0,8')
ventlist.append('3,4 -> 9,4')
ventlist.append('2,1 -> 2,2')
ventlist.append('7,0 -> 7,4')
ventlist.append('6,4 -> 2,0')
ventlist.append('0,9 -> 2,9')
ventlist.append('1,4 -> 3,4')
ventlist.append('0,0 -> 8,8')
ventlist.append('5,5 -> 8,2')

def all_points(list):
    pointlist = []
    for all in list:
        if all[0] == all[7]:
            x = 0
            while int(all[2]) + x <= int(all[9]):
                pointa = str(all[0])
                pointb = str(int(all[2]) + x)
                pointlist.append(f'{pointa},{pointb}')
                x += 1
        elif all[2] == all[9]:
            x = 0
            while int(all[0]) + x <= int(all[7]):
                pointa = str(int(all[0]) + x)
                pointb = str(all[2])
                pointlist.append(f'{pointa},{pointb}')
                x += 1
        else:
            if all[0] < all[7] and all[2] < all[9]:
                x = 0
                while int(all[0]) + x <= int(all[7]):
                    pointa = str(int(all[0]) + x)
                    pointb = str(int(all[2]) + x)
                    pointlist.append(f'{pointa},{pointb}')
                    x += 1
            if all[0] > all[7] and all[2] < all[9]:
                x = 0
                while int(all[0]) - x >= int(all[7]):
                    pointa = str(int(all[0]) - x)
                    pointb = str(int(all[2]) + x)
                    pointlist.append(f'{pointa},{pointb}')
                    x += 1
            if all[0] > all[7] and all[2] > all[9]:
                x = 0
                while int(all[0]) - x >= int(all[7]):
                    pointa = str(int(all[0]) - x)
                    pointb = str(int(all[2]) - x)
                    pointlist.append(f'{pointa},{pointb}')
                    x += 1
            if all[0] < all[7] and all[2] > all[9]:
                x = 0
                while int(all[0]) + x <= int(all[7]):
                    pointa = str(int(all[0]) + x)
                    pointb = str(int(all[2]) - x)
                    pointlist.append(f'{pointa},{pointb}')
                    x += 1
    return pointlist

def remove_singles(list):
    newlist = list.copy()
    print(newlist)
    g = 0
    for all in list:
        current = all
        try:
            newlist.remove(current)
        except ValueError:
            continue
        if current in newlist:
            g += 1
            newlist.remove(current)
            if current in newlist:
                newlist.remove(current)
                if current in newlist:
                    newlist.remove(current)
            continue
        
    return g

print(remove_singles(all_points(ventlist)))
        
