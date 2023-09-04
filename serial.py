import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
import random
import string


class SerialCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel()
        self.generate_button = QPushButton('Generate')

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.generate_button)
        self.setLayout(main_layout)

        self.generate_button.clicked.connect(self.generate_code)

        self.setWindowTitle('Serial Code Generator')
        self.setGeometry(100, 200, 300, 100)
        self.show()

    def generate_code(self):
        code = ''.join(random.choices(string.digits, k=6))
        self.label.setText(f'Serial Code: {code}')
        self.label.setFont(QFont('Arial', 14))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = SerialCodeGenerator()
    sys.exit(app.exec())
