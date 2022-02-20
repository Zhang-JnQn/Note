from PIL import Image
import os
import random

imglist_name = []
imglist = []
bbxlist_name = []
#bbxlist = []


def get_img(inputpath):
    file_list = os.listdir(inputpath)
    last_path = inputpath
    for filename in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量
        # 否则每次只能遍历一层目录
        cur_path = os.path.join(inputpath, filename)
        if filename == "classes.txt":
            continue
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            last_path = cur_path
            # self.show_path_file(cur_path)
        elif os.path.splitext(filename)[1] == ".jpg":
            filename = os.path.join(last_path, filename)
            imglist_name.append(filename)
            # imglist.append(cv2.imread(filename))
            imglist.append(Image.open(filename))
        elif os.path.splitext(filename)[1] == ".txt":
            filename = os.path.join(last_path, filename)
            bbxlist_name.append(filename)
            # bbxlist.append()


def scale_data():

    for index in range(len(imglist)):
        img = imglist[index]
        imx, imy = img.size
        bckgnd = Image.new('RGB', (imx, imy), (105+random.randint(-105, 150),
                           105+random.randint(-105, 150), 105+random.randint(-105, 150)))
        #bckgnd_cpy = Image.new('RGB', (imx, imy), (105+random.randint(-105, 150),
           #                    105+random.randint(-105, 150), 105+random.randint(-105, 150)))
        #bckgnd_cp = Image.new('RGB', (imx, imy), (105+random.randint(-105, 150),
        #                       105+random.randint(-105, 150), 105+random.randint(-105, 150)))
        imx = imx//2
        imy = imy//2
        img = img.resize((imx, imy), Image.ANTIALIAS)
        bckgnd.paste(img, (0, 0))
        #img = img.resize((imx//2, imy//2), Image.ANTIALIAS)
        #bckgnd_cpy.paste(img, (0, 0))
        #img = img.resize((imx//4, imy//4), Image.ANTIALIAS)
        #bckgnd_cp.paste(img,(0,0))
        #matplotlib.pyplot.imshow(bckgnd)
        #bckgnd.show()
        bckgnd.save(imglist_name[index].split(".jpg", 1)[0]+"_half.jpg")
        #bckgnd_cpy.save(imglist_name[index].split(".jpg", 1)[0]+"_quat.jpg")
        #bckgnd_cp.save(imglist_name[index].split(".jpg",1)[0]+"_small.jpg")

        file = open(bbxlist_name[index])

        for line in file.readlines():
            dataMat = []
            curLine = line.strip().split(" ")
            # 这里使用的是map函数直接把数据转化成为float类型
            floatLine = list(map(float, curLine))
            for i in range(4):
                dataMat.append(floatLine[1:][i])
            print(dataMat)
            newBBox = open(bbxlist_name[index].split(
                ".txt", 1)[0]+"_half.txt", 'a')
            newBBox.write(str(int(floatLine[0])))
            for data in dataMat:
                data = data/2
                newBBox.write(' ')
                newBBox.write('%.6f' % (data))
            newBBox.write('\n')

            #quatBBox = open(bbxlist_name[index].split(
               # ".txt", 1)[0]+"_quat.txt", 'a')
            #quatBBox.write(str(int(floatLine[0])))
            #for data in dataMat:
                #data = data/4
                #quatBBox.write(' ')
               # quatBBox.write('%.6f' % (data))
            #quatBBox.write('\n')

            #smallBBox = open(bbxlist_name[index].split(
            #    ".txt", 1)[0]+"_small.txt", 'a')
         #   smallBBox.write(str(int(floatLine[0])))
      #      for data in dataMat:
   #             data = data/8
#                smallBBox.write(' ')
#                smallBBox.write('%.6f' % (data))
#            smallBBox.write('\n')


if __name__ == "__main__":
    inputpath = "/home/inori/datasets/extend/aug"
    get_img(inputpath)
    scale_data()

