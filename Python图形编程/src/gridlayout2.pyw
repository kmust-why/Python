#coding=utf-8
# function:网格布局管理器

from PyQt4 import QtGui
import sys


class GridLayout(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        # 设置窗口标题
        self.setWindowTitle(u'迷你写字板')
        # 设置三个标签
        title = QtGui.QLabel(u'标题')
        author = QtGui.QLabel(u'作者')
        review = QtGui.QLabel(u'预览')

        # 设置三个单行文本框
        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QLineEdit()
        # 定义网格布局管理器
        grid = QtGui.QGridLayout()
        # 设置网格的间隔
        grid.setSpacing(10)

        # 将title放到（1，0）
        grid.addWidget(title,1,0)
        # 将titleEdit放到（1，1）
        grid.addWidget(titleEdit,1,1)

        # 将author放到（2，0）
        grid.addWidget(author,2,0)
        # 将authorEdit放到（2，1）
        grid.addWidget(authorEdit,2,1)
        
        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)

        # 设置该主窗口的布局为网格布局
        self.setLayout(grid)
        # 设置该主窗口的大小
        self.resize(350,300)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    qb = GridLayout()
    qb.show()
    sys.exit(app.exec_())