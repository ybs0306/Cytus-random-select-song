import os.path
import random

class select:
    def __init__(self):
        self.songlist = os.path.isfile('songlist.txt')
        self.data = []
        self.load()

    def load(self):
        if self.songlist:
            with open("songlist.txt", 'r', encoding='big5') as f:
                for line in f:
                    try:
                        items = line.strip('\n').split('\t',1)
                        self.data.append(items)
                    except Exception as e:
                        print('分析歌曲清單檔案錯誤\n{e}'.format(e=str(e)))
        else:
            print('找不到歌曲表')

    def run(self):
        while True:
            input_num = input('輸入要抽幾首: ')
            if input_num.isdigit() == True:
                input_num = int(input_num)
                if input_num >= 0:
                    for x in range(0, input_num):
                        r = random.randint(0, len(self.data))
                        print('{id} - {song}'.format(
                            id=self.data[r][0],
                            song=self.data[r][1]
                            ))
                    break
            else:
                print("輸入格式錯囉")

selectSong = select()
selectSong.run()
