import sys
import random
import qrcode
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Create an application object
app = QApplication(sys.argv)

# Create a main window
window = QMainWindow()

# Create a label widget for the title
title = QLabel(window, text="QR Code Generator")

# Create a line edit widget for the name input
name_input = QLineEdit(window, placeholderText="Enter a name")

# Create a label widget for the data output
data_output = QLabel(window)

# Create a label widget for the QR code image
qr_image = QLabel(window)

# Create a button widget for the QR code generation
qr_button = QPushButton(window, text="Generate QR Code")

# Define a function to generate the QR code
def generate_qr_code():
    # Get the name from the line edit widget
    name = name_input.text()

    # Generate a random number between 100000 and 999999
    number = random.randint(100000, 999999)

    # Concatenate the name and number with a space
    data = name + " " + str(number)

    # Set the data output label text to the data
    data_output.setText(data)

    # Create a QR code image from the data
    img = qrcode.make(data)

    # Convert the image to a QPixmap object
    pixmap = QPixmap.fromImage(img.toImage())

    # Set the QR code image label pixmap to the pixmap
    qr_image.setPixmap(pixmap)

# Connect the button click signal to the generate QR code function
qr_button.clicked.connect(generate_qr_code)

# Create a vertical layout manager
layout = QVBoxLayout()

# Add the widgets to the layout manager
layout.addWidget(title)
layout.addWidget(name_input)
layout.addWidget(data_output)
layout.addWidget(qr_image)
layout.addWidget(qr_button)

# Create a widget object
widget = QWidget()

# Set the layout object as its layout
widget.setLayout(layout)

# Set the widget object as the central widget of the window
window.setCentralWidget(widget)

# Show the window and start the main loop
window.show()
app.exec_()
