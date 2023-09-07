# This module contains a class that generates serial numbers for names.

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from random import randint

class SerialCodeGenerator(QWidget):
    """This class is a PyQt widget that generates serial numbers for names."""

    def __init__(self):
        """This method initializes the widget and its components."""

        # Call the parent class constructor
        super().__init__()

        # Set the window title
        self.setWindowTitle('Serial Code Generator')

        # Create a line edit widget for the name
        self.name_input = QLineEdit()

        # Create a label widget for the output
        self.label = QLabel()

        # Create a button widget for generating the serial number
        self.generate_button = QPushButton('Generate')

        # Connect the button to the generate_code method
        self.generate_button.clicked.connect(self.generate_code)

        # Create a vertical layout widget to arrange the widgets vertically
        layout = QVBoxLayout()

        # Add the widgets to the layout
        layout.addWidget(self.name_input)
        layout.addWidget(self.label)
        layout.addWidget(self.generate_button)

        # Set the layout as the main layout of the widget
        self.setLayout(layout)

    def generate_code(self):
        """This method generates a serial number for the name entered by the user."""

        # Get the name from the line edit and capitalize it
        name = self.name_input.text().capitalize()

        # Check if the name is empty
        if not name:
            # Display an error message on the label
            self.label.setText('Please enter a name.')
            return

        # Generate a random six-digit number as the serial number
        serial_number = ''.join([str(randint(0, 9)) for i in range(6)])

        # Display the name and the serial number on the label
        self.label.setText(f'Name: {name}\nSerial Number: {serial_number}')

if __name__ == '__main__':
    # Create a Qt application object
    app = QApplication([])

    # Create an instance of the widget
    widget = SerialCodeGenerator()

    # Show the widget on the screen
    widget.show()

    # Start the main event loop of the application
    app.exec_()
