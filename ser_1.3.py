''' import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QFont
import random
import string


class SerialCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.name_input = QLineEdit()
        self.label = QLabel()
        self.generate_button = QPushButton('Generate')

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.name_input)
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.generate_button)
        self.setLayout(main_layout)

        self.generate_button.clicked.connect(self.generate_code)

        self.setWindowTitle('Serial Code Generator')
        self.setGeometry(100, 200, 300, 150)
        self.show()

    def generate_code(self):
        name = self.name_input.text()
        if not name:
            self.label.setText('Please enter a name.')
            return

        random_part = ''.join(random.choices(string.digits, k=6))
        serial_code = f'{name.upper()}-{random_part}'
        self.label.setText(f'Serial Code: {serial_code}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = SerialCodeGenerator()
    sys.exit(app.exec())'''


'''import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QFont
import random
import string

class SerialCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.name_input = QLineEdit()
        self.label = QLabel()
        self.generate_button = QPushButton('Generate')

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.name_input)
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.generate_button)
        self.setLayout(main_layout)

        self.generate_button.clicked.connect(self.generate_code)

        self.setWindowTitle('Serial Code Generator')
        self.setGeometry(100, 200, 300, 150)
        self.show()

    def generate_code(self):
        name = self.name_input.text().capitalize()
        if not name:
            self.label.setText('Please enter a name.')
            return

        random_part = ''.join(random.choices(string.digits, k=6))
        serial_code = f'{random_part}'

        # Put the name and serial number in separate columns
        self.label.setText(f'Name: {name}\nSerial Number: {serial_code}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = SerialCodeGenerator()
    sys.exit(app.exec())'''


import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QFont, QColor
import random
import string

class SerialCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.name_input = QLineEdit()
        self.label = QLabel()
        self.generate_button = QPushButton('Generate')

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.name_input)
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.generate_button)
        self.setLayout(main_layout)

        self.generate_button.clicked.connect(self.generate_code)

        self.setWindowTitle('Serial Code Generator')
        self.setGeometry(100, 200, 300, 150)
        self.show()

    def generate_code(self):
        name = self.name_input.text().capitalize()
        if not name:
            self.label.setText('Please enter a name.')
            return

        random_part = ''.join(random.choices(string.digits, k=6))
        serial_code = f'{random_part}'

        # Put the name and serial number in separate columns
        self.label.setText(f'Name: <font color="red">{name}</font>\nSerial Number: <font color="blue">{serial_code}</font>')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = SerialCodeGenerator()
    sys.exit(app.exec())

