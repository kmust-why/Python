#-*- coding=utf-8 -*-
# function:演示居中的用法

import sys

from PyQt4 import QtGui

class Center(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        # 设置标题
        self.setWindowTitle(u'居中')
        # 设置大小
        self.resize(550,450)
        # 执行center函数
        self.center()
    
    def center(self):
        # 获取电脑的屏幕大小
        screen = QtGui.QDesktopWidget().screenGeometry()
        # 获取当前主窗口的大小
        size = self.geometry()
        # 将当前的主窗口的位置移动到如下
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    qb = Center()
    qb.show()
    sys.exit(app.exec_())