# This module contains a class that generates serial numbers for names.

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from random import randint

class SerialCodeGenerator(App):
    """This class is a Kivy app that generates serial numbers for names."""

    def build(self):
        """This method builds the user interface of the app."""

        # Create a text input widget for the name
        self.name_input = TextInput()

        # Create a label widget for the output
        self.label = Label()

        # Create a button widget for generating the serial number
        self.generate_button = Button(text='Generate')

        # Bind the button to the generate_code method
        self.generate_button.bind(on_press=self.generate_code)

        # Create a box layout widget to arrange the widgets vertically
        layout = BoxLayout(orientation='vertical')

        # Add the widgets to the layout
        layout.add_widget(self.name_input)
        layout.add_widget(self.label)
        layout.add_widget(self.generate_button)

        # Return the layout as the root widget of the app
        return layout

    def generate_code(self, instance):
        """This method generates a serial number for the name entered by the user."""

        # Get the name from the text input and capitalize it
        name = self.name_input.text.capitalize()

        # Check if the name is empty
        if not name:
            # Display an error message on the label
            self.label.text = 'Please enter a name.'
            return

        # Generate a random six-digit number as the serial number
        serial_number = ''.join([str(randint(0, 9)) for i in range(6)])

        # Display the name and the serial number on the label
        self.label.text = f'Name: {name}\nSerial Number: {serial_number}'

if __name__ == '__main__':
    # Run the app
    SerialCodeGenerator().run()
