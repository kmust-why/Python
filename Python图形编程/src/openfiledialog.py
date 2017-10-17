#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: openfiledialog.py
#time: 2017/10/17 9:32
# function:演示打开文件对话框的内容

from PyQt4 import QtGui,QtCore
import sys

# 定义一个类，继承QtGui.QMainWindow类
class OpenFileDialog(QtGui.QMainWindow):
    # 定义构造函数
    def __init__(self,parent=None):
        # 调用父类的构造函数
        QtGui.QMainWindow.__init__(self,parent)
        # 设置主窗口的title
        self.setWindowTitle(u'打开文件')
        # 定义一个多行文本框
        self.textEdit = QtGui.QTextEdit()
        # 将该文本框放置到该主窗口的中心位置
        self.setCentralWidget(self.textEdit)
        # 定义一个状态栏
        self.statusBar()
        # 设置焦点
        self.setFocus()
        # 设置一个工具栏
        exit = QtGui.QAction(QtGui.QIcon('open.ico'),u'打开',self)
        # 为该工具栏创建一个快捷键
        exit.setShortcut('Ctrl+Q')
        # 为该工具栏添加一个状态栏的提示，当鼠标移动到该工具栏上的时候
        exit.setStatusTip(u'打开新文件')
        # 为该工具栏绑定相应的事件,当点击该工具栏的时候就会执行showDialog这个函数
        self.connect(exit,QtCore.SIGNAL('triggered()'),self.showDialog)

        # 定义一个菜单栏
        menubar = self.menuBar()
        # 添加名为File的菜单
        file = menubar.addMenu('&File')
        # 在该菜单下添加二级菜单
        file.addAction(exit)
        # 设置主窗口的位置和大小
        self.setGeometry(300,300,350,250)

    def showDialog(self):
        # 打开一个文件对话框，该函数返回一个文件名
        filename = QtGui.QFileDialog.getOpenFileName(self,u'打开文件','./')
        if filename:
            # 打开文件
            with open(filename,'r') as file:
                # 读取该文件的内容
                data = file.read()
                # 把读取的文件内容读取到文本框中
                self.textEdit.setText(data)
        else:
            return


# 程序的入口
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # 创建一个penfiledialog对象
    penfiledialog = OpenFileDialog()
    # 显示quitbutton对象
    penfiledialog.show()
    sys.exit(app.exec_())
