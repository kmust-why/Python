#!/usr/bin/env python
# encoding: utf-8
# function:演示Box布局，有一个布局的嵌套关系
from PyQt4 import QtGui
import sys

class Boxlayout(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        # 设置标题
        self.setWindowTitle(u'Box布局')
        
        ok = QtGui.QPushButton(u'确定')
        cancel = QtGui.QPushButton(u'取消')
        
        hbox = QtGui.QHBoxLayout()
        # 设置一个间隔
        hbox.addStretch(1)
        # 将相关的按钮添加到其内
        hbox.addWidget(ok)
        hbox.addWidget(cancel)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        self.resize(400,250)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    qb = Boxlayout()
    qb.show()
    sys.exit(app.exec_())