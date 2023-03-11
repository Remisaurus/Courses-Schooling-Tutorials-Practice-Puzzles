senders = []

with open ('mbox-short.txt', 'r') as input:
    for line in input:
        if line.startswith("From "):
                s = line.split(" ")
                senders.append(s[1])
        else:
            continue
        
# print(f'{senders}\n' , len(senders))

domainnames = {}

for sender in senders:
    splitatat = sender.split("@")
    if splitatat[1] not in domainnames:
        domainnames[splitatat[1]] = 1
    else:
        domainnames[splitatat[1]] += 1
        
        
print(domainnames)
    