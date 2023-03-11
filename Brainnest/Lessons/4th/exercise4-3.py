senders = []

with open ('mbox-short.txt', 'r') as input:
    for line in input:
        if line.startswith("From "):
                s = line.split(" ")
                senders.append(s[1])
        else:
            continue
        
print(f'{senders}\n' , len(senders))