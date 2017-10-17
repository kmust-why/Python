#coding=utf-8，
# function:演示复选框的用法

import sys

from PyQt4 import QtGui,QtCore
class CheckBox(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)

        # 设置主窗口的位置和大小
        self.setGeometry(300,300,250,150)
        # 设置主窗口的标题
        self.setWindowTitle(u'单选框')
        # 创建一个checkbox对象
        self.cb = QtGui.QCheckBox(u'美女，选我啊',self)
        # 设置该复选框的焦点模式为：无焦点
        self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
        # 设置复选框的位置
        self.cb.move(10,10)
        # 绑定事件，表示该复选框的状态改变的时候，就执行changeTitle函数
        self.connect(self.cb,QtCore.SIGNAL('stateChanged(int)'),self.changeTitle)
        
    def changeTitle(self,value):
        if self.cb.isChecked():
            # 如果该复选框被选中了，则将主窗口的标题设置为如下所示
            self.setWindowTitle(u'单选框')
        else:
            self.setWindowTitle(u'没有选中')

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = CheckBox()
    w.show()
    sys.exit(app.exec_())