
#pyinstaller -F main.py
# -- coding: utf-8 --

import os
import tkinter
import tkinter.ttk
from tkinter import filedialog
from PIL import Image
import shutil

# --------------------------------------------------------------

def del_files(dir_path):
    filelist=os.listdir(dir_path)
    for filename in filelist:
        filepath=os.path.join(dir_path,filename)
        os.remove(filepath)
    print('remove all file ok')

def picPathopen():
    path = filedialog.askdirectory()
    picPath.set(path)

def resizePic(pic_path):
    n = 0
     # 进度值最大值
    progressbar['maximum'] = 100
    # 进度值初始值
    progressbar['value'] = 0
    num = 100 / len(os.listdir(pic_path))
    fileList=os.listdir(pic_path)
    for i in fileList:
    #设置旧文件名（就是路径+文件名）
        oldPic = pic_path + os.sep + fileList[n]  # os.sep添加系统分隔符
        im1 = Image.open(oldPic)
        im2 = im1.resize((int(picWidth.get()),int(picHeight.get())))
        im2.save(os.path.join(pic_path,oldPic))
        progressbar['value'] += num
        top.update()
        n+=1

def copyAndRenamePic():
    if picPath.get() == '':
        newNum.set('**请选择图片路径**')
        return
    #获取该目录下所有文件，存入列表中
    fileList=os.listdir(picPath.get())
    newPicPath = os.path.abspath(os.path.dirname(picPath.get())) + os.sep + picName.get()
    if os.path.exists(newPicPath):
        del_files(newPicPath)
    else:
        os.makedirs(newPicPath)
    m = 0
    n = 0
    o = 0
    for i in fileList:
    #设置旧文件名（就是路径+文件名）
        oldPic = picPath.get() + os.sep + fileList[n]  # os.sep添加系统分隔符
        #设置新文件名
        if n == m:
            m = m + int(spaceNum.get()) + 1
            newpic = newPicPath + os.sep + picName.get() + '0' + str(o)+'.png'
            o+=1
            # im1 = Image.open(oldPic)
            # im2 = im1.resize((int(picWidth.get()),int(picHeight.get())))
            # im2.save(os.path.join(newPicPath,newpic))
            # newNum.set(o)
            shutil.copy(oldPic, newpic)
        n+=1
    resizePic(newPicPath)
    newNum.set('**图片处理完成**')
    os.system("explorer.exe %s" % newPicPath)


def renamePic():
    #获取该目录下所有文件，存入列表中
    fileList=os.listdir(picPath.get())
    for i in fileList:
    #设置旧文件名（就是路径+文件名）
        oldname = picPath.get() + os.sep + fileList[int(i)]  # os.sep添加系统分隔符
        #设置新文件名
        newname = picPath.get() + os.sep + picName.get() + '0' + str(i)+'.png'
        os.rename(oldname,newname)  #用os模块中的rename方法对文件改名

def buttonHandler():
    copyAndRenamePic()


top = tkinter.Tk()
top.geometry('500x300')
Offsety = 40
top.title("图片批量处理工具")

# --------------------------------------------------------------
newNum = tkinter.StringVar(value='')
o = tkinter.Label(top, width = 50, textvariable = newNum,fg='#ff0000')
o.place(x = 100, y = Offsety*0, width=300, height=25)

a = tkinter.Label(top, bd =5, width = 10, text = "图片路径：")
a.place(x = 10, y = Offsety*1, width=80, height=25)

picPath = tkinter.StringVar(value='')
b = tkinter.Entry(top, bd =5, width = 40,textvariable=picPath)
b.place(x = 85, y = Offsety*1, width=340, height=25)

c = tkinter.Button(top, text ="打开", command = picPathopen)
c.place(x = 425, y = Offsety*1, width=60, height=25)

d = tkinter.Label(top, bd =5, width = 10, text = "图片尺寸：")
d.place(x = 10, y = Offsety*2, width=80, height=25)

picWidth = tkinter.StringVar(value='512')
e = tkinter.Entry(top, bd =5, width = 40,textvariable=picWidth)
e.place(x = 85, y = Offsety*2, width=100, height=25)

picHeight = tkinter.StringVar(value='512')
f = tkinter.Entry(top, bd =5, width = 40,textvariable=picHeight)
f.place(x = 200, y = Offsety*2, width=100, height=25)

g = tkinter.Label(top, bd =5, width = 10, text = "修改文件名：")
g.place(x = 10, y = Offsety*3, width=80, height=25)

picName = tkinter.StringVar(value='pic')
h = tkinter.Entry(top, bd =5, width = 40,textvariable=picName)
h.place(x = 85, y = Offsety*3, width=200, height=25)

i = tkinter.Label(top, bd =5, width = 10, text = "抽帧间隔：")
i.place(x = 10, y = Offsety*4, width=80, height=25)

spaceNum = tkinter.StringVar(value='0')
j = tkinter.Entry(top, bd =5, width = 40,textvariable=spaceNum)
j.place(x = 85, y = Offsety*4, width=100, height=25)

# --------------------------------------------------------------

l = tkinter.Button(top, text ="开始生成", command = buttonHandler)
l.place(x = 215, y = Offsety*5, width=85, height=40)

progressbar = tkinter.ttk.Progressbar(top)
progressbar.place(x = 50, y = Offsety*6.5, width=400)

# 进入消息循环
top.mainloop()



