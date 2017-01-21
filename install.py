""" install fontman

Fontman installer application.
This script is to determine platform type and run the appropriate py script.
"""

import platform

from PyQt4 import QtGui, QtCore, uic


# gather system information
system = platform.system()
arch = platform.architecture()


def print_info():
    print("detected system: " + str(system))
    print("detected architecture: " + str(arch[0]))


def p(x):
    print(x)


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        uic.loadUi('redirect.ui', self)

        print('Opening installer...')
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.stdout_ready)
        self.process.readyReadStandardError.connect(self.stderr_ready)
        self.process.started.connect(lambda: p('Started!'))
        self.process.finished.connect(lambda: p('Finished!'))

        print('Starting process')

        if "Windows" in system:
            self.process.start('python', ['windows.py'])
        elif "Linux" in system:
            self.process.start('python3', ['linux.py'])

    def append(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor);

    def stdout_ready(self):
        text = str(self.process.readAllStandardOutput(), encoding='utf-8')
        print(text.strip())
        self.append(text)

    def stderr_ready(self):
        text = str(self.process.readAllStandardError(), encoding='utf-8')
        print(text.strip())
        self.append(text)


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
