#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: tooltip.py
#time: 2017/10/16 18:04
# function:气泡提示
from PyQt4 import QtGui
import sys

# 定义一个类，继承QtGui.QWidget类
class ToolTip(QtGui.QWidget):
    # 定义构造函数
    def __init__(self,parent=None):
        # 调用父类的构造函数
        QtGui.QWidget.__init__(self,parent)
        # 设置位置及大小
        self.setGeometry(500,500,600,400)
        # 设置窗口的标题
        self.setWindowTitle('ToolTip')
        # 设置气泡提示的信息
        self.setToolTip('this is ToolTip.')
        # 设置QToolTip的颜色
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish',10))

# 程序的入口
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # 创建一个tooltip对象
    tooltip = ToolTip()
    # 显示tooltip对象
    tooltip.show()
    sys.exit(app.exec_())
