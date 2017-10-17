#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: menubar.py
#time: 2017/10/17 10:28
# function:演示菜单栏的用法

from PyQt4 import QtGui,QtCore
import sys

# 定义一个类，继承QtGui.QMainWindow类
class MenuBar(QtGui.QMainWindow):
    # 定义构造函数
    def __init__(self,parent=None):
        # 调用父类的构造函数
        QtGui.QMainWindow.__init__(self,parent)
        # 设置主窗口的title
        self.setWindowTitle(u'菜单')
        # 设置主窗口的位置和大小
        self.setGeometry(300, 300, 250, 150)
        # 设置一个QAction对象
        exit = QtGui.QAction(QtGui.QIcon('exit.png'),u'退出',self)

        # 为该QAction添加快捷键
        exit.setShortcut('Ctrl+Q')
        # 设置状态栏的信息
        exit.setStatusTip(u'退出程序')
        # 绑定事件
        exit.connect(exit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT('quit()'))

        # 定义一个状态栏
        self.statusBar()

        # 定义一个存放菜单的容器
        menubar = self.menuBar()
        # 在该容器中添加菜单
        file = menubar.addMenu('&File')
        # 在该菜单下添加二级菜单
        file.addAction(exit)


# 程序的入口
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # 创建一个menubar对象
    menubar = MenuBar()
    # 显示sigslot对象
    menubar.show()
    sys.exit(app.exec_())
