from setup_ui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.goBtn)
        self.comboBox.activated.connect(self.deviceBtn)

    def goBtn(self):
        print(self.comboBox.currentText())
        print(self.spinBox_3.value())  # trials SpinBox

    def deviceBtn(self):
        print(self.comboBox.currentText())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
