import os
bboxlist_name = []
#bboxlist = []
# 首先遍历当前目录所有文件及文件夹
inputpath = '/home/inori/datasets/extend/aug/'
file_list = os.listdir(inputpath)
last_path = inputpath
for filename in file_list:
    # 利用os.path.join()方法取得路径全名，并存入cur_path变量
    # 否则每次只能遍历一层目录
    cur_path = os.path.join(inputpath, filename)
    # 判断是否是文件夹
    if os.path.isdir(cur_path):
        last_path = cur_path
        # self.show_path_file(cur_path)
    elif os.path.splitext(filename)[1] == ".txt":
        filename = os.path.join(last_path, filename)
        bboxlist_name.append(filename)
for index in range(len(bboxlist_name)):
    for count in range(20):
        filename = bboxlist_name[index].split(".txt", 1)[0]
        filename = filename + "-" + str(count) + ".txt"
        os.popen('cp {0} {1}'.format(bboxlist_name[index], filename))
