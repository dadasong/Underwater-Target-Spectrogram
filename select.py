#-*- coding:utf-8 -*-
import os

def imageSelect(path):
    train_string = ''
    train_label_string = ''
    test_string = ''
    test_label_string = ''
    #遍历目录
    files = os.listdir(path)
    for f in files:
        files_2 = os.listdir(path+"/"+f)

        img_num = len(files_2)  #每一个文件夹下的图片数目
        count = 0   #计数 每类图片的80%用于训练 20%用于测试
        for f2 in files_2:
            if "bmp" in f2 and count < int(img_num*0.8):
                count += 1
                #把路径写入训练集
                train_string += path + '/' + f + '/' + f2 + '\n'
                #写入类别
                train_label_string += f[1:] + '\n'
            if "bmp" in f2 and count >= int(img_num*0.8):
                count += 1
                #把路径写入测试集
                test_string += path + '/' + f + '/' + f2 + '\n'
                test_label_string += f[1:] + '\n'

    #完成遍历 写入文件
    writeFile("train.txt",train_string)
    writeFile("train_label.txt",train_label_string)
    writeFile("test.txt",test_string)
    writeFile("test_label.txt",test_label_string)

def writeFile(filename , write_string):
    f = open(filename , 'w')
    f.write(write_string)
    f.close()

if __name__ == "__main__":
    imageSelect("C:/Users/Administrator/Desktop/UnderwaterSepctrogram")
    