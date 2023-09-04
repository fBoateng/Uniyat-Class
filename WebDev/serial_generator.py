import sys
import random
import string
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class SerialCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel('Click "Generate" to get your serial code:', self)
        self.label.setFont(self.label.font().family(), 14)
        font = QtGui.QFont("Arial", 14)
        self.label.setFont(font)

        self.output_label = QLabel('', self)
        self.output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output_label.setFont(self.label.font().family(), 18)

        generate_button = QPushButton('Generate', self)
        generate_button.clicked.connect(self.generate_code)

        exit_button = QPushButton('Exit', self)
        exit_button.clicked.connect(self.close)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.output_label)
        vbox.addWidget(generate_button)
        vbox.addWidget(exit_button)

        self.setLayout(vbox)

        self.setWindowTitle('Serial Code Generator')
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def generate_code(self):
        self.output_label.setText(''.join(random.choices(string.ascii_letters + string.digits, k=6)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = SerialCodeGenerator()
    sys.exit(app.exec())
