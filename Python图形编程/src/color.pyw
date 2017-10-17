#coding=utf-8
# function:演示颜色的用法
import sys


from PyQt4 import QtGui, QtCore

class ColorDialog(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        # 创建一个颜色对象
        color = QtGui.QColor(255, 255, 255)
        # 设置主窗口的位置和大小
        self.setGeometry(300, 300, 250, 180)
        # 设置主窗口的标题
        self.setWindowTitle(u'颜色选择盘')
        # 创建一个按钮对象
        self.button = QtGui.QPushButton(u'选择颜色', self)
        # 设置按钮的焦点模式
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        # 设置按钮的位置
        self.button.move(20, 20)
        # 绑定事件
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
        # 使设置的焦点模式生效
        self.setFocus()
        # 创建一个QWidget对象
        self.widget = QtGui.QWidget(self)
        # 设置该wiget的背景颜色
        self.widget.setStyleSheet('QWidget {background-color: %s}' %color.name())
        # 设置该widget的位置和大小
        self.widget.setGeometry(130, 22, 100, 100)
    def showDialog(self):
        # 创建一个颜色对话框
        col = QtGui.QColorDialog.getColor()
        # 查看该颜色是有有效
        if col.isValid():
            # 有效，则设置widget的背景颜色
            self.widget.setStyleSheet('QWidget {background-color: %s}' %col.name())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    qb = ColorDialog()
    qb.show()
    sys.exit(app.exec_())