import sys
from PyQt5.QtWidgets import QApplication
from motogui2 import Ui_MainWindow
from PyQt5 import QtWidgets


class MotoGui(QtWidgets.QMainWindow):
    def __init__(self):
        super(MotoGui, self).__init__()

        # Set up the user interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(self.close)

    # override standard close event
    def closeEvent(self, event):
        answer = QtWidgets.QMessageBox.question(
            self,
            'Leaving Already?',
            'Exit Moto-Logger?',
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No)
        if answer == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MotoGui()
    window.show()
    sys.exit(app.exec_())
