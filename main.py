import random

data = []
with open("Cytus song list.txt", 'r') as f:
    for line in f:
        items = line.strip('\n').split('\t',1)
        data.append(items)

r = random.randint(0,210)
print('{ID} - {song}'.format(ID=data[r][0],song=data[r][1]))
