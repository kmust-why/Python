#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: sliderlabel.py
#time: 2017/10/16 21:29
# function:演示滑动块

from PyQt4 import QtGui,QtCore
import sys

# 定义一个类，继承QtGui.QMainWindow类
class SliderLabel(QtGui.QWidget):
    # 定义构造函数
    def __init__(self,parent=None):
        # 调用父类的构造函数
        QtGui.QWidget.__init__(self,parent)
        # 设置位置及大小
        self.setGeometry(200,200,1500,600)
        # 设置窗口的标题
        self.setWindowTitle(u'滑动块')
        # 设置滑动块对象，QtCore.Qt.Horizontal表示该滑动块水平放置
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal,self)
        # 设置滑动块的聚焦策略
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        # 设置滑动块的位置和大小
        self.slider.setGeometry(30,40,100,60)
        # 表示当滑动块的值发生改变的时候就执行那个changValue函数
        self.connect(self.slider,QtCore.SIGNAL('valueChanged(int)'),self.changValue)
        # 创建一个标签对象
        self.label = QtGui.QLabel(self)
        # 为该标签添加一个图标
        self.label.setPixmap(QtGui.QPixmap('01.png'))
        # 设置标签的位置
        self.label.setGeometry(160,40,1400,600)

    def changValue(self,value):
        # 获取滑动块的值
        pos = self.slider.value()
        # 如果滑动块处于初始状态，则显示第一张
        if pos == 0:
            self.label.setPixmap(QtGui.QPixmap('01.png'))
        elif 0 < pos <=30:
            self.label.setPixmap(QtGui.QPixmap('02.png'))
        elif 30 < pos < 80:
            self.label.setPixmap(QtGui.QPixmap('03.png'))
        else:
            self.label.setPixmap(QtGui.QPixmap('04.png'))



# 程序的入口
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # 创建一个sliderlabel对象
    sliderlabel = SliderLabel()
    # 显示sliderlabel对象
    sliderlabel.show()
    sys.exit(app.exec_())




