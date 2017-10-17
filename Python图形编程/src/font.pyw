#coding=utf-8
# function：演示字体的用法
import sys

from PyQt4 import QtGui, QtCore


class FontDialog(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        # 创建一个垂直布局管理器对象，即为一个容器
        hbox = QtGui.QHBoxLayout()
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 250, 110)
        # 设置窗口的标题
        self.setWindowTitle(u'字体对话框')
        # 创建一个按钮对象
        button = QtGui.QPushButton(u'选择字体', self)
        # 设置按钮的焦点策略
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        # 设置按钮的位置
        button.move(20, 20)
        # 将按钮添加到容器中
        hbox.addWidget(button)
        # 为按钮绑定事件
        self.connect(button, QtCore.SIGNAL('clicked()'), self.showDialog)
        # 创建一个标签对象
        self.label = QtGui.QLabel(u'我要学点编程', self)
        # 设置标签的位置
        self.label.move(130, 20)
        # 将标签添加到容器中
        hbox.addWidget(self.label, 1)
        # 设置该主窗口的布局为垂直布局
        self.setLayout(hbox)
    def showDialog(self):
        # 创建一个颜色对话框，第一个参数表示返回的字体，第二个参数表示按下那个键
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            # 设置标签的字体
            self.label.setFont(font)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    cd = FontDialog()
    cd.show()
    sys.exit(app.exec_())