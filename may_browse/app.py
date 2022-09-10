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

from PyQt5.QtWidgets import QApplication
import os
import sys
from may_browse import window

def execute(argv):
    app = QApplication(sys.argv)
    app.setApplicationName("may-browse")
    win = window.Window()

    win.createTab()
    win.switchTab(0)

    #win.createTab()
    #win.switchTab(1)
    #win.tabs[win.currentTab].url("http://www.youtube.com")

    app.exec_()

if __name__ == "__main__":
    execute(sys.argv[1:])