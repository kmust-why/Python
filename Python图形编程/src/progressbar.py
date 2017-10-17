#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: progressbar.py
#time: 2017/10/17 8:59
# 演示进度条

from PyQt4 import QtGui,QtCore
import sys

# 定义一个类，继承QtGui.QMainWindow类
class ProgressBar(QtGui.QWidget):
    # 定义构造函数
    def __init__(self,parent=None):
        # 调用父类的构造函数
        QtGui.QWidget.__init__(self,parent)
        # 设置主窗口的title
        self.setWindowTitle(u'进度条')
        # 设置主窗口的位置和大小
        self.setGeometry(300, 300, 250, 150)
        # 定义一个进度条
        self.pbar = QtGui.QProgressBar(self)
        # 设置进度条的位置和大小
        self.pbar.setGeometry(30, 40, 200, 25)
        # 定义一个按钮
        self.button = QtGui.QPushButton(u'开始',self)
        # 设置按钮为无焦点模式
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        # 设置按钮的位置
        self.button.move(40,80)
        # 为按钮添加相应的事件操作,当点击该按钮的时候就执行onStart函数
        self.connect(self.button,QtCore.SIGNAL('clicked()'),self.onStart)

        # 定义一个定时器
        self.timer = QtCore.QBasicTimer()
        self.step = 0

    def timerEvent(self, event):
        if self.step >= 100:
            # 如果步长值大于100
            self.timer.stop()
            # 最后返回
            return
        # 否则步长加一
        self.step = self.step + 1
        # 将进度条的显示值设置为当前的step值
        self.pbar.setValue(self.step)

    def onStart(self):
        # 判断定时器当前是否处于工作状态
        if self.timer.isActive():
            # 如果处于工作状态，则停止该定时器
            self.timer.stop()
            # 设置按钮上的值为开始
            self.button.setText(u'开始')
        else:
            # 否则该定时器没有在工作
            # 开启该定时器，定时器每隔100ms就去执行一次timerEvent函数
            self.timer.start(100,self)
            # 将按钮上的文字设置为停止
            self.button.setText(u'停止')


# 程序的入口
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # 创建一个quitbutton对象
    progressbar = ProgressBar()
    # 显示sigslot对象
    progressbar.show()
    sys.exit(app.exec_())
