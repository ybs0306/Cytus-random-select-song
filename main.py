import random

data = []
with open("Cytus song list.txt", 'r') as f:
    for line in f:
        items = line.strip('\n').split('\t',1)
        data.append(items)

loop = 1
print("輸入要抽幾首:")

while True:
    try:
        loop = int(input('\n'))
        if loop >= 0:
            for x in range(0,loop):
                r = random.randint(0,210)
                print('{ID} - {song}'.format(ID=data[r][0],song=data[r][1]))
        else:
            print("輸入格式錯囉")
    except:
        print("輸入格式錯囉")

    if loop == 0:
        break
