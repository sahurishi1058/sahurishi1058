import PyQt5 as Qt1
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QGridLayout,QRadioButton, QCheckBox, QLineEdit, QTextEdit, QComboBox, QSlider, QProgressBar, QTabWidget, QTreeWidget, QTableWidget, QFormLayout, QScrollArea)
from PyQt5.QtGui import QIcon, QFont, QPixmap    
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Example3")
        self.setWindowIcon(QIcon(r"C:\Users\sahur\sahurishi1058\Screenshot 2025-04-17 114636.png"))
        self.setGeometry(700, 300, 500, 400)
        self.button=QPushButton("Click Me", self)
        self.initUI()
    def initUI(self):
        self.button.setGeometry(50, 50, 100, 30)
        self.button.setStyleSheet("background-color: lightblue; color: black; font-size: 16px;")
        self.button.clicked.connect(self.on_button_click)
        pass
    def on_button_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.Disabled = True
        pass
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()