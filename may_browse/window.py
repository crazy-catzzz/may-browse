#!/usr/bin/env python3

#    Copyright (C) 2022  crazy-catzzz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow, QStackedWidget
import tab

class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.show()
        self.central = QStackedWidget()
        self.setCentralWidget(self.central)
    tabs = []
    currentTab = 0

    def createTab(self):
        self.tabs.append(tab.Tab("http://www.google.com"))
        self.central.addWidget(self.tabs[-1].view)

    def switchTab(self, index):
        self.currentTab = index
        self.central.setCurrentIndex(index)