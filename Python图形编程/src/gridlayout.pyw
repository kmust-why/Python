#!/usr/bin/env python
# encoding: utf-8
# function:使用网格布局来布局计算器
from PyQt4 import QtGui
import sys


class GrildLayout(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        # 设置窗口的标题
        self.setWindowTitle(u'计算器布局图')
        names = [u'清除',u'后退','',u'关闭','7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
        # 定义一个网格布局管理器
        grid = QtGui.QGridLayout()
        j = 0
        pos = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3),(4,0),(4,1),(4,2),(4,3)]
        for i in names:
            button = QtGui.QPushButton(i)
            if j == 2:
                grid.addWidget(QtGui.QLabel(''),0,2)
            else:
                # 添加按钮
                grid.addWidget(button,pos[j][0],pos[j][1])
            j += 1
        # 设置窗口的布局为网格布局
        self.setLayout(grid)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    qb = GrildLayout()
    qb.show()
    sys.exit(app.exec_())