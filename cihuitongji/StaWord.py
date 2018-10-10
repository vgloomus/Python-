import re
import io
import os
from matplotlib import pyplot as plt

def draw(data,num):
    data1 = data[:num]
    for word in data1:
        plt.bar(word[1:],word[:-1])

    plt.legend()
    plt.xlabel('words')
    plt.ylabel('rate')
    plt.title(' 46 level high frequency words')
    plt.show()




def input(file_path,data):
    with io.open(file_path, 'w', encoding='utf-8') as f:
        for i in data:
            f.write(str(i))
            f.write('\n')


def comm(path):
    path1 = os.path.abspath('.')
    out_path2 = path + '\\3\\' + '2' + '.txt'
    num = 1
    txt_path = path + '\\2\\'
    files = os.listdir(txt_path)
    test1 = dict()
    for f in files:
        file_path = txt_path + f
        with io.open(file_path,'r') as f1:
            data = f1.read()
            words = [s.lower() for s in re.findall('[a-zA-Z]+', data)]
            badwords = ['the', 'and', 'that', 'are', 'for']
            for word in words:
                if len(word) > 2 and word not in  badwords:
                    test1[word] = test1.get(word,0) + 1

    test2 = sorted(test1.items(),key=lambda x: x[1],reverse=True).copy()
    input(out_path2,test2)
    draw(test2,10)

