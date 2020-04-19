from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from validators import url, domain
from clipboard import copy, paste
import pyshorteners
import threading

# Action Class Contains Actions Of Menu App
class actions:

    auto = False

    def short():
        s = pyshorteners.Shortener()
        link = paste()
        short = s.dagd.short(link)
        copy(short)
        print(f'{link} || {short}')

"""
    def autoshort():
        s = pyshorteners.Shortener()
        while True: 
            print('Running')
            link = paste()
            if not url(link) or not domain(link):
                return
            short = s.dagd.short(link)
            copy(short)
"""
    def turnAutoOn():
        actions.auto = True



class debug:
    def itjustworks():
        print('Yup it works')

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Create The Icon
icon = QIcon("../imgs/icon.png")

# Create The Tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create The Menu
menu = QMenu()

# Shorten Link From Clipbrd When Triggered
short = QAction('Shorten')
short.triggered.connect(actions.short)
menu.addAction(short)

"""
# AtuShorten Links In Clipbrd
autoshort = QAction('AutoShort')
autoshort.triggered.connect(actions.autoshort)
menu.addAction(autoshort)
"""

# FeedBack Button Redirect
feedback = QAction('Share FeedBack')
menu.addAction(feedback)

# Preferences Window
prefs = QAction('Preferences')
menu.addAction(prefs)

# Quit App When Triggered
quit = QAction('Quit')
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)

app.exec_()
