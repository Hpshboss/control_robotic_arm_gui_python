import serial
import sys
from PyQt5.QtWidgets import QMainWindow
import GUI
from PyQt5.QtWidgets import QApplication


class Main(QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.import_pushbutton)
        self.pushButton_2.clicked.connect(self.enter_pushbutton)
        self.pushButton_3.clicked.connect(self.stop_pushbutton)
        self.pushButton_4.clicked.connect(self.g_pushbutton)

    def import_pushbutton(self):
        print("Import button")
        try:
            import_data = open(self.lineEdit.text(), "r")
            self.textEdit.append(import_data.read())
        except:
            print("failed import")

    def enter_pushbutton(self):
        print("Enter button")
        text_buffer = self.textEdit.toPlainText()
        text_buffer_list = text_buffer.splitlines()
        print(text_buffer_list[-1])
        try:
            robotic_arm = serial.Serial("COM", 9600)
            robotic_arm.write(self.textEdit.toPlainText())
            robotic_arm.read(50)
        except:
            print("failed enter")

    def stop_pushbutton(self):
        print("Stop button")

    def g_pushbutton(self):
        print("G button")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())

