#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
ZetCode PyQt5 tutorial 
 
This example shows a tooltip on
a window and a button.
 
author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""
 
import sys
from PyQt6.QtWidgets import (QWidget, QToolTip, QPushButton, QLabel, QApplication)
from PyQt6.QtGui import QFont    
 
class Example(QWidget):
 
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
 
        QToolTip.setFont(QFont('SansSerif', 10))
 
        self.setToolTip('This is a <b>QWidget</b> widget')
 
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       

        label = QLabel('账号', self)
        label.move(50,100)
        label.setGeometry(50, 100, 200, 100)

        self.setGeometry(300, 300, 1500, 1000)
        self.setWindowTitle('Tooltips')
        self.show()
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())