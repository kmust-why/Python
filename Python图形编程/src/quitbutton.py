#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: quitbutton.py
#time: 2017/10/17 8:49
# 演示退出按钮的效果

from PyQt4 import QtGui,QtCore
import sys

# 定义一个类，继承QtGui.QMainWindow类
class QuitButton(QtGui.QWidget):
    # 定义构造函数
    def __init__(self,parent=None):
        # 调用父类的构造函数
        QtGui.QWidget.__init__(self,parent)
        # 设置主窗口的title
        self.setWindowTitle(u'退出按钮的作用')
        # 设置主窗口的位置和大小
        self.setGeometry(300,300,350,250)
        # 定义一个pushbutton
        quit = QtGui.QPushButton(u'关闭',self)
        # 设置按钮的位置和大小
        quit.setGeometry(10,10,60,35)
        # 为按钮绑定相关的事件，当点击该按钮的时候，就退出该程序
        self.connect(quit,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))


# 程序的入口
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # 创建一个quitbutton对象
    quitbutton = QuitButton()
    # 显示quitbutton对象
    quitbutton.show()
    sys.exit(app.exec_())
