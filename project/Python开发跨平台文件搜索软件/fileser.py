from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import tkinter.scrolledtext
import os
import fnmatch

"""
1、界面的设计与开发
2、功能的完善

"""


def func1():
    str1 = ent1.get()
    str2 = ent2.get()
    if not (str1 and str2):
        tkinter.messagebox.showinfo('温馨提示', '请输入关键词和文件类型，再选择文件夹')
        return
    fn = tkinter.filedialog.askdirectory()  # 选择一个文件夹路径
    if not fn:
        return
    listbox.delete(0, END)
    # 遍历路径下的所有文件和目录
    fnlist = os.walk(fn)
    # for i in fnlist:
    # print(i)
    for root, dir, files in fnlist:
        for i in fnmatch.filter(files, str2):
            with open(root + '/' + i, 'r', encoding='utf-8') as fn:
                content = fn.read()
            if str1 in content:
                listbox.insert(END, root + '/' + i)


def func2(event):
    # 取出双击的坐标
    # print(listbox.curselection())
    if not listbox.curselection():
        return
    window = Tk()
    window.title('文件查看')
    # 带下拉框的多行文本框
    text = tkinter.scrolledtext.ScrolledText(window, width=100)
    text.grid()
    path = listbox.get(listbox.curselection(), last=None)
    with open(path, 'r', encoding='utf-8') as fn:
        text.insert(END, fn.read())


if __name__ == '__main__':
    # 其中Tk是一个类
    root = Tk()
    root.title('文件搜索利器')
    root.geometry('+500+200')
    Label(root, text='搜索词').grid()
    ent1 = Entry(root)
    ent1.grid(row=0, column=1)  # row横坐标，column纵坐标
    Label(root, text='文件类型').grid(row=0, column=2)
    ent2 = Entry(root)
    ent2.grid(row=0, column=3)  # row横坐标，column纵坐标
    btn = Button(root, text='选择文件', command=func1)
    btn.grid(row=0, column=4)
    var1 = StringVar()
    # print(var1)
    # print(type(var1))
    listbox = Listbox(root, width=80, listvariable=var1)
    listbox.bind('<Double-Button-1>', func2)
    listbox.grid(row=1, column=0, columnspan=5)
    root.mainloop()
