import os
import shutil


destination = 'C:\\Users\\Belzebub\\Desktop\\Memes'
for i in os.walk('C:\\Users\\Belzebub\\Desktop'):
    for j in i:
        if 'jpg' in str(j):
            arr = [x for x in j if 'jpg' and 'meme' in str(x)]

for i in arr:
    shutil.copy('C:\\Users\\Belzebub\\Desktop\\'+f'{i}', destination)