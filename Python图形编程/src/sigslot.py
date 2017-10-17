#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: sigslot.py
#time: 2017/10/17 8:32
# 演示信号与槽

from PyQt4 import QtGui,QtCore
import sys

# 定义一个类，继承QtGui.QMainWindow类
class SigSlot(QtGui.QWidget):
    # 定义构造函数
    def __init__(self,parent=None):
        # 调用父类的构造函数
        QtGui.QWidget.__init__(self,parent)
        # 设置主窗口的title
        self.setWindowTitle(u'事件驱动测试')
        # 定义一个显示数字的LCD
        lcd = QtGui.QLCDNumber(self)
        # 定义一个水平的滑动块
        slider = QtGui.QSlider(QtCore.Qt.Horizontal,self)

        # 定义一个盒子的布局管理器
        vbox = QtGui.QVBoxLayout()
        # 将显示数字的LCD放到该盒子中去
        vbox.addWidget(lcd)
        # 将该水平滑动块放到该盒子中去
        vbox.addWidget(slider)

        # 设置该SigSlot的布局
        self.setLayout(vbox)
        # 设置与滑动块相对应的事件,表示当滑动块的值改变的时候，lcd显示的值也随之而改变
        self.connect(slider,QtCore.SIGNAL('valueChanged(int)'),lcd,QtCore.SLOT('display(int)'))
        # 设置主窗口的大小
        self.resize(350,250)


# 程序的入口
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # 创建一个sigslot对象
    sigslot = SigSlot()
    # 显示sigslot对象
    sigslot.show()
    sys.exit(app.exec_())
