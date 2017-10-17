#coding=utf-8
# function:演示输入对话框
import sys


from PyQt4 import QtGui,QtCore

class InputDialog(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        
        self.setGeometry(300,300,350,80)
        self.setWindowTitle(u'输入对话框')
        self.button = QtGui.QPushButton(u'对话',self)
        # 设置焦点为无焦点
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20,20)
        self.connect(self.button,QtCore.SIGNAL('clicked()'),self.showDialog)
        # 让焦点设置生效
        self.setFocus()

        # 定义一个单行文本框
        self.label = QtGui.QLineEdit(self)
        # 设置单行文本框的位置
        self.label.move(130,22)
    
    def showDialog(self):
        # 定义一个输入对话框，该函数的返回值：第一个表示返回输入的内容，第二个参数表示点击的是那个按钮
        text, ok = QtGui.QInputDialog.getText(self,u'输入对话框',u'输入姓名：')
        
        if ok :
            # 将返回的内容放到单行文本框中去
            self.label.setText(unicode(text))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    icon = InputDialog()
    icon.show()
    sys.exit(app.exec_())