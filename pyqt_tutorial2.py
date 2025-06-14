import PyQt5 as Qt1
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel,QHBoxLayout,QGridLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Example2")
        self.setWindowIcon(QIcon(r"C:\Users\sahur\sahurishi1058\Screenshot 2025-04-17 114636.png"))
        self.setGeometry(700,300, 500, 400)
        label = QLabel("Hello, PyQt5!", self)
        self.setGeometry(0,0,500,500)
        pix_img= QPixmap(r"C:\Users\sahur\sahurishi1058\Screenshot 2025-04-17 114636.png")
        label.setPixmap(pix_img)
        label.setScaledContents(True)
        label.setGeometry(self.width(), 0,500,500)
        self.initUI()
    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)
        lable1= QLabel("Label 1")
        label2= QLabel("Label 2")
        label3= QLabel("Label 3")
        vbox= QVBoxLayout()
        # hbox= QHBoxLayout()
        # gbox= QGridLayout()
        vbox.addWidget(lable1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        central_widget.setLayout(vbox)

        pass
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()