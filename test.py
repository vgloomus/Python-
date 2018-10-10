import sys, os
import WordTxt2
import StaWord

path1 = os.path.abspath('.')

def run():
    WordTxt2.closesoft()
    path = 'D:\Python-learning\cihuitongji'
    WordTxt2.Translate(path)

    StaWord.comm(path)

if __name__ == '__main__':
    run()
