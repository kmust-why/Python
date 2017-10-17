#coding=utf-8
# function:演示日历的用法
import sys

from PyQt4 import QtGui, QtCore

class Calendar(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle(u'日历')
        # 创建一个日历对象
        self.cal = QtGui.QCalendarWidget(self)
        # 设置日历的格点可见
        self.cal.setGridVisible(True)
        # 绑定事件，表示当日历的选择改变的时候就执行showDate函数
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'),self.showDate)
        # 创建一个label对象
        self.label = QtGui.QLabel(self)
        # 获取到日历默认选择到的日期
        date = self.cal.selectedDate()
        # 将获取到的日期显示到label上
        self.label.setText(str(date.toPyDate()))
        # 创建一个水平布局管理器
        vbox = QtGui.QVBoxLayout()
        # 将cal添加到水平布局管理器容器中
        vbox.addWidget(self.cal)
        # 将label添加到水平布局管理器容器中
        vbox.addWidget(self.label)
        # 设置主窗口的布局
        self.setLayout(vbox)
        
    def showDate(self):
        # 获取到被选择的日期
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = Calendar()
    w.show()
    sys.exit(app.exec_())