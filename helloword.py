import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import pyqtgraph


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.text_label = QLabel()
        self.text_label.setText("Hello World!")
        self.text_label.setFont(QFont('Arial', 20))/' /p'

        self.button = QPushButton("Fancy Button")
        self.button.setFont(QFont('Arial', 14))
        self.button.clicked.connect(lambda: self.text_label.setText("Changed!"))

        self.setGeometry(50, 50, 300, 200)
        self.setWindowTitle("PyQt5 Example")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text_label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    app.exec()
