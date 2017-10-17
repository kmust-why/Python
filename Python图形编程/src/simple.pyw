#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# function:显示一个主窗口
# 导入相关的包
from PyQt4 import QtGui
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 创建一个app，参数为系统传递过来的系统参数
app = QtGui.QApplication(sys.argv)
# 创建一个widget对象，即一个主窗口
widget = QtGui.QWidget()
# 设置主窗口的大小
widget.resize(600,400)
# 设置主窗口的标题
widget.setWindowTitle('simple')
# 显示出主窗口
widget.show()
# 退出程序
sys.exit(app.exec_())

