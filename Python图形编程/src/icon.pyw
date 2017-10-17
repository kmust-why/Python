#!/usr/bin/env python
# encoding: utf-8
# function:设置窗口的图标
import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Icon')
        # 为该窗体添加一个图标
        self.setWindowIcon(QtGui.QIcon('mail.ico'))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    icon = Icon()
    icon.show()
    sys.exit(app.exec_())
