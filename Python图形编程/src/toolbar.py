#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: ToolBar.py
#time: 2017/10/16 18:23
# 演示工具栏

from PyQt4 import QtGui,QtCore
import sys

# 定义一个类，继承QtGui.QMainWindow类
class ToolBar(QtGui.QMainWindow):
    # 定义构造函数
    def __init__(self,parent=None):
        # 调用父类的构造函数
        QtGui.QMainWindow.__init__(self,parent)
        # 设置位置及大小
        self.setGeometry(500,500,600,400)
        # 设置窗口的标题
        self.setWindowTitle(u'工具栏')
        # 添加一个QAction对象，即添加一个工具栏按钮
        self.exit = QtGui.QAction(QtGui.QIcon('exit.png'),u'退出',self)
        # 为该工具栏添加一个快捷键
        self.exit.setShortcut('Ctrl+Q')
        # 为该工具栏按钮添加相应的事件操作,表示当鼠标点击该工具栏的时候，就执行退出的操作
        self.connect(self.exit,QtCore.SIGNAL('triggered()'),QtGui.qApp,QtCore.SLOT('quit()'))
        # 创建一个存放工具栏的容器
        self.toolbar = self.addToolBar(u'退出')
        # 将工具栏里面加入到其中
        self.toolbar.addAction(self.exit)


# 程序的入口
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # 创建一个tooltip对象
    toolbar = ToolBar()
    # 显示tooltip对象
    toolbar.show()
    sys.exit(app.exec_())



