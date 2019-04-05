import serial
import sys
from PyQt5.QtWidgets import QMainWindow
import GUI
from PyQt5.QtWidgets import QApplication


class Main(QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())

# class App(GUI.QtWidgets.QMainWindow, GUI.Ui_MainWindow):
#     def __init__(self):
#         super(App, self).__init__()
#         self.ui = GUI.Ui_MainWindow
#         self.title = 'PyQt5 simple window'
#         self.ui.setupUi(self)
#
#
# if __name__ == '__main__':
#     app = GUI.QtWidgets.QApplication(sys.argv)
#     ex = App()
#     ex.show()
#     sys.exit(app.exec_())
