from tkinter import *
import tkinter.filedialog


def newfile():
    txt = text.get(1.0,END)
    if not txt:
        return
    savefile()
    #print('new')

def openfile():

    filename = tkinter.filedialog.askopenfilename(title='打开文档',filetypes=[('文本文档', '*.txt'), ('python文件', '*.py')])
    if not filename:
        return
    fn = open(filename,'r')
    txt = fn.read()
    fn.close()
    text.insert(1.0,txt)
    root.title('%s - 记事本' % filename.split('/')[-1])
    #print(filename)
    #print(type)

def savefile():
    filename = tkinter.filedialog.asksaveasfilename(title='另存为...',initialfile='未命名.txt',filetypes=[('文本文档','*.txt'),('python文件','*.py')],defaultextension='.txt')
    if not filename:
        return
    fn = open(filename,'w')
    fn.write(text.get(1.0,END))
    fn.close()
    text.delete(1.0,END)
    root.title('%s - 记事本' %filename.split('/')[-1])
    #print(filename)

def saveas():
    print('saveas')
#其中Tk是一个类
root = Tk()
root.title('无标题 - 记事本')
root.geometry('300x200+600+300')
me = Menu()#菜单栏
root.config(menu=me)
filemenu = Menu(me) #二级菜单
filemenu.add_command(label='新建',accelerator='Ctrl + N',command=newfile)
filemenu.add_command(label='打开',accelerator='Ctrl + O',command=openfile)
filemenu.add_command(label='保存',accelerator='Ctrl + S',command=savefile)
filemenu.add_command(label='另存为',command=saveas)
filemenu.add_separator()
filemenu.add_command(label='页面设置')
filemenu.add_command(label='打印')
filemenu.add_separator()
filemenu.add_command(label='退出',command=root.quit)

me.add_cascade(label='文件',menu=filemenu)
#编辑区
text = Text() #多行文本框
text.pack()
#me.add_cascade(label='文件',menu=filemenu)
root.mainloop()
