from win32com import client as wc
import os
path1 = os.path.abspath('.')
all_FileNum = 1


def closesoft():
    print(''' 挂在程序关闭中
    ''')
    import win32com
    import win32com.client
    wc = win32com.client.constants

    try:
        wps = win32com.client.gencache.EnsureDispatch('kwps.application')
    #except:
        #wps = win32com.client.gencache.EnsureDispatch('wps.application')
    except:
        wps = win32com.client.gencache.EnsureDispatch('word.application')

    try:
        wps.Documents.Close()
        wps.Documents.Close(wc.wdDoNotSaveChanges)
        wps.Quit
    except:
        pass

# 程序本质改变文件后缀名进行统计
def Translate(path):

    global all_FileNum
    doc_path = path + '\\1\\'
    txt_path = path + '\\2\\'
    files = os.listdir(doc_path)
    for f in files:
        if (f[0] == '~' or f[0] == '.'):
            continue
        new = doc_path + f
        print('word2txt' + str(all_FileNum))
        tmp = txt_path + str(all_FileNum)
        word = wc.Dispatch('Word.Application')
        doc = word.Documents.Open(new)
        doc.SaveAs(tmp + '.txt' , 4)
        all_FileNum = all_FileNum + 1
    doc.Close()
    word.Quit()

if __name__ == '__main__':
    path = 'D:\Python-learning\cihuitongji'
    Translate(path)
    print('文件总数= ',all_FileNum)