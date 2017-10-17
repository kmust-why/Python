#!/usr/bin/env python
# encoding: utf-8
from PyQt4 import QtGui,QtCore
import sys


class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self)
        # 设置主窗口的大小
        self.resize(350,250)
        # 设置标题
        self.setWindowTitle(u'主界面')
        # 定义一个多行文本框
        textEdit = QtGui.QTextEdit()
        # 将文本框置于中间位置
        self.setCentralWidget(textEdit)

        # 设置一个QAction对象
        exit = QtGui.QAction(QtGui.QIcon('exit.png'), u'退出', self)

        # 为该QAction添加快捷键
        exit.setShortcut('Ctrl+Q')
        # 设置状态栏的信息
        exit.setStatusTip(u'退出程序')
        # 绑定事件
        exit.connect(exit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT('quit()'))

        # 定义一个状态栏
        self.statusBar()

        # 定义一个存放菜单的容器
        menubar = self.menuBar()
        # 在该容器中添加菜单
        file = menubar.addMenu('&File')
        # 在该菜单下添加二级菜单
        file.addAction(exit)

        # 定义一个存放工具按钮的容器
        toolbar = self.addToolBar('Exit')
        # 在该容器内放入该工具按钮
        toolbar.addAction(exit)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())