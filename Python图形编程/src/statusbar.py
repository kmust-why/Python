#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: statusbar.py
#time: 2017/10/16 18:17
# function:显示状态栏

#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: tooltip.py
#time: 2017/10/16 18:04
from PyQt4 import QtGui
import sys

# 定义一个类，继承QtGui.QMainWindow类
class StatusBar(QtGui.QMainWindow):
    # 定义构造函数
    def __init__(self,parent=None):
        # 调用父类的构造函数
        QtGui.QMainWindow.__init__(self,parent)
        # 设置位置及大小
        self.setGeometry(500,500,600,400)
        # 设置窗口的标题
        self.setWindowTitle('StatusBar')
        # 设置状态栏的信息
        self.statusBar().showMessage(u'this is StatusBar.这是状态栏')


# 程序的入口
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # 创建一个tooltip对象
    statusbar = StatusBar()
    # 显示tooltip对象
    statusbar.show()
    sys.exit(app.exec_())

