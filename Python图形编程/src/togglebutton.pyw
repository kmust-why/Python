#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: togglebutton.py
#time: 2017/10/16 21:55
# function:演示五颜六色的效果


from PyQt4 import QtGui,QtCore
import sys

# 定义一个类，继承QtGui.QMainWindow类
class ToggleButton(QtGui.QWidget):
    # 定义构造函数
    def __init__(self,parent=None):
        # 调用父类的构造函数
        QtGui.QWidget.__init__(self,parent)
        # 设置一个颜色对象，白色
        self.color = QtGui.QColor(0,0,0)
        # 设置主窗口的位置和大小
        self.setGeometry(300, 300, 280, 170)
        # 设置主窗口的标题
        self.setWindowTitle(u'五颜六色')

        # 设置一个红色按钮
        self.red = QtGui.QPushButton(u'红色',self)
        # 设置该按钮为可复选的按钮
        self.red.setCheckable(True)
        # 设置该按钮在主窗口中的位置
        self.red.move(10,10)
        # 为该按钮添加相关的事件操作
        self.connect(self.red,QtCore.SIGNAL('clicked()'),self.setRed)

        # 同理创建后面的两个按钮

        self.green = QtGui.QPushButton(u'绿色', self)
        self.green.setCheckable(True)
        self.green.move(10, 60)
        self.connect(self.green, QtCore.SIGNAL('clicked()'), self.setGreen)

        self.blue = QtGui.QPushButton(u'蓝色', self)
        self.blue.setCheckable(True)
        self.blue.move(10, 110)
        self.connect(self.blue, QtCore.SIGNAL('clicked()'), self.setBlue)

        # 创建一个QWidget对象
        self.square = QtGui.QWidget(self)
        # 设置该QWidget对象的位置和大小
        self.square.setGeometry(150, 20, 100, 100)
        # 设置该QWidget对象的样式，设置其的背景为白色
        self.square.setStyleSheet('QWidget{background-color:%s}' %self.color.name())
        # 表示清除样式，给其一个默认的样式
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('cleanlooks'))

    def setRed(self):
        if self.red.isChecked():
            # 表示红色按钮被按下
            self.color.setRed(255)
        else:
            self.color.setRed(0)
        # 将该QWidget对象设置为相应的背景颜色
        self.square.setStyleSheet('QWidget{background-color:%s}' %self.color.name())

    def setGreen(self):
        if self.green.isChecked():
            # 表示红色按钮被按下
            self.color.setGreen(255)
        else:
            self.color.setGreen(0)
        # 将该QWidget对象设置为相应的背景颜色
        self.square.setStyleSheet('QWidget{background-color:%s}' % self.color.name())

    def setBlue(self):
        if self.blue.isChecked():
            # 表示红色按钮被按下
            self.color.setBlue(255)
        else:
            self.color.setBlue(0)
        # 将该QWidget对象设置为相应的背景颜色
        self.square.setStyleSheet('QWidget{background-color:%s}' % self.color.name())



# 程序的入口
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # 创建一个togglebutton对象
    togglebutton = ToggleButton()
    # 显示togglebutton对象
    togglebutton.show()
    sys.exit(app.exec_())





