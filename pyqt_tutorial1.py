import sys
import PyQt5 as Qt1
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Example")
        self.setWindowIcon(QIcon(r"C:\Users\sahur\sahurishi1058\Screenshot 2025-04-17 114636.png"))
        # self.setGeometry(100, 100, 600, 400)
        label=QLabel("Hello, PyQt5!", self)
        label.setFont(QFont("Arial", 18))
        self.setGeometry(0, 0, 600, 400)
        label.setStyleSheet("color: blue;""background-color: yellow;""font-weight: bold;""font-size: 20px;")
        label.setAlignment(Qt.AlignRight)



def main():
    app= QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    pass
if __name__ == "__main__":
    main()


    