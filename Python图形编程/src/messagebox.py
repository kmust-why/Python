#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: messagebox.py
#time: 2017/10/17 10:13
# function:演示消息框

from PyQt4 import QtGui,QtCore
import sys

# 定义一个类，继承QtGui.QMainWindow类
class MessageBox(QtGui.QWidget):
    # 定义构造函数
    def __init__(self,parent=None):
        # 调用父类的构造函数
        QtGui.QWidget.__init__(self,parent)
        # 设置主窗口的title
        self.setWindowTitle(u'消息窗口')
        # 设置主窗口的位置和大小
        self.setGeometry(300, 300, 250, 150)

    def closeEvent(self, QCloseEvent):
        reply = QtGui.QMessageBox.question(self,u'警告',u'确认退出',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            # 如果点击了yes，则执行QCloseEvent.accept(),关闭该消息窗口
            QCloseEvent.accept()
        else:
            # 否则就忽略掉
            QCloseEvent.ignore()


# 程序的入口
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # 创建一个messagebox对象
    messagebox = MessageBox()
    # 显示messagebox对象
    messagebox.show()
    sys.exit(app.exec_())

