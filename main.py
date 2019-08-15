import serial
import sys
import os
from PyQt5.QtWidgets import QMainWindow
import GUI
from PyQt5.QtWidgets import QApplication


class Main(QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.import_pushbutton)
        self.pushButton_2.clicked.connect(self.enter_pushbutton)
        self.pushButton_4.clicked.connect(self.stop_pushbutton)
        self.pushButton_3.clicked.connect(self.g_pushbutton)

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
            robotic_arm = serial.Serial("COM8", 9600, xonxoff=True, timeout= 0.5)
            robotic_arm.write(self.textEdit.toPlainText().encode() + os.linesep.encode())
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
        except:
            print("failed enter")

    def stop_pushbutton(self):
        print("Stop button")
        try:
            robotic_arm = serial.Serial("COM8", 9600, xonxoff=True, timeout=0.5)
            robotic_arm.write("EXIT".encode() + os.linesep.encode())
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
        except:
            print("failed Stop")

    def g_pushbutton(self):
        print("G button")
        try:
            robotic_arm = serial.Serial("COM8", 9600, xonxoff=True, timeout=0.5)
            robotic_arm.write("G".encode() + os.linesep.encode())
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
            print(robotic_arm.readline(50))
        except:
            print("failed G")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())

