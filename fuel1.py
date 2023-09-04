# price of diesel per litre 14.481
# price of diesel per gallon 14.481

# price of petrol per litre 11.501
# price of petrol per gallon 43.536

# amount_being_bought = float(input('Please enter the amount you are buying? '))


# def conv():
#    litre = amount_being_bought / 11.501
#       return litre


# petrol = conv()
# print(petrol)


'''def qnty_litre():
    user_input = input('Please are you buying per litre or per gallon? ')
    if user_input == 'litre':
        fuelamount = float(input('How much are you buying? '))
        try:
            if user_input == 'litre':
                litre = fuelamount / 11.501
        except:
            if user_input < price_per_litre:
                print('Amount can not be purchased.')
    return litre


def qnty_gallon():
    user_input = input('Please are you buying per litre or per gallon? ')
    if user_input == 'gallon':
        fuelamount = float(input('How much are you buying? '))
        if user_input == 'gallon':
            gallon = fuelamount / 43.536
    return gallon'''

'''price_per_litre = 11.501


def qnty_purchased():
    user_input = float(input('How much are you buying? '))
    if user_input <= price_per_litre:
        print('Invalid Amount entered.')
    amount_purchased = user_input / price_per_litre
    print(f'You are buying {user_input} cedis worth {amount_purchased} litres.)


qnty_purchased()'''
'''import sys
from PyQt5.QtWidgets import QApplication, QWidget


class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Empty Window in PyQt')


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())'''

'''import PySimpleGUI as sg
from datetime import datetime

sg.theme('Black')

layout = [[sg.Text("Enter full name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
          [sg.Text("Enter your passport number:"), sg.Input(key='-PASSPORT_NUMBER-', do_not_clear=True, size=(10, 1))],
          # "RADIO" makes the radio buttons part of the same group, so when you click one, the other will be unchecked
          [sg.Radio("Male", "RADIO", key='-MALE-'), sg.Radio("Female", "RADIO", key='-FEMALE-')],
          [sg.Input(key='-DEPARTURE-', size=(20, 1)),
           sg.CalendarButton("DATE OF DEPARTURE", close_when_date_chosen=True, target='-DEPARTURE-', location=(0, 0),
                             no_titlebar=False)],
          [sg.Input(key='-ARRIVAL-', size=(20, 1)),
           sg.CalendarButton("DATE OF ARRIVAL", close_when_date_chosen=True, target='-ARRIVAL-', location=(0, 0),
                             no_titlebar=False)],
          [sg.Text('Choose your destination:', size=(30, 1), font='Lucida', justification='left')],
          # Formatting is weird on Mac - also need to change number of rows based on desired appearance
          [sg.Listbox(values=['Havana', 'Moscow', 'Beijing', 'Tehran', 'Damascus', 'Tripoli', 'Sanaa'], size=(40, 5),
                      select_mode='single', key='-DESTINATION-')],
          [sg.Button('Reserve Ticket'), sg.Exit()]
          ]

window = sg.Window('привет Airlines', layout)


# This is to make sure that the arrival date is not before the departure date
def is_arrival_before_departure(departure_string, arrival_string):
    # 2021-08-01 13:09:43
    departure_object = datetime.strptime(departure_string, '%Y-%m-%d %H:%M:%S')
    arrival_object = datetime.strptime(arrival_string, '%Y-%m-%d %H:%M:%S')
    return arrival_object < departure_object


def validate(values):
    is_valid = True
    values_invalid = []

    if len(values['-NAME-']) == 0:
        values_invalid.append('Name')
        is_valid = False

    if values['-PASSPORT_NUMBER-'].isnumeric:
        values_invalid.append('Passport Number')
        is_valid = False

    if not values['-MALE-'] and not values['-FEMALE-']:
        values_invalid.append('Gender')
        is_valid = False

    if len(values['-DEPARTURE-']) == 0:
        values_invalid.append('Departure Date')
        is_valid = False

    if len(values['-ARRIVAL-']) == 0:
        values_invalid.append('Arrival Date')
        is_valid = False

    if len(values['-DEPARTURE-']) != 0 and len(values['-ARRIVAL-']) != 0 and is_arrival_before_departure(
            values['-DEPARTURE-'], values['-ARRIVAL-']):
        values_invalid.append('Arrival Date comes before Departure Date')
        is_valid = False

    # This is how you handle a case when an error may occur
    try:
        print(values['-DESTINATION-'][0])
    except:
        values_invalid.append('Destination')
        is_valid = False

    result = [is_valid, values_invalid]
    return result


def generate_error_message(values_invalid):
    error_message = ''
    for value_invalid in values_invalid:
        error_message += ('\nInvalid' + ':' + value_invalid)

    return error_message


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Reserve Ticket':
        validation_result = validate(values)
        if validation_result[0]:
            sg.popup('Flight Reservation submitted!')
        else:
            error_message = generate_error_message(validation_result[1])
            sg.popup(error_message)
window.close()'''


# 1. Instead of importing the entire datetime library, only import the required function `strptime` and use it as `from datetime import datetime, strptime`.
# 2. Change `isnumeric` to `isnumeric()` in line 44 to actually call the function.
# 3. Use `if not values.get('-NAME-'):` instead of `if len(values['-NAME-']) == 0:` to check for an empty string.
# 4. Use `if not values.get('-PASSPORT_NUMBER-').isnumeric():` instead of `if values['-PASSPORT_NUMBER-'].isnumeric:` to check if the passport number is valid.
# 5. Replace the list `values_invalid` with a single string `error_message` which keeps track of all errored fields.
# 6. Remove the try-except block around `values['-DESTINATION-'][0]` and use `if not values.get('-DESTINATION-'):` instead to check if a destination is selected.

# The optimized code would look like this:


# 1. Move the conversion of departure and arrival dates to datetime objects inside the validate function to avoid unnecessary processing if the form is not submitted.
# 2. Change the if statements that check for emptiness of certain inputs to use the "not" operator directly on the values of the inputs.
# 3. Use a dictionary to store the keys and error messages related to each input, instead of concatenating the error message string.
# 4. Use the "event == sg.WIN_CLOSED" condition directly in the while loop to avoid an additional if statement inside the loop.
# 5. Remove unnecessary "no_titlebar" and "location" arguments in the calendar buttons.
# 6. Add a default value for the list box to avoid an error when no option is selected.

# Here's the optimized code:

import PySimpleGUI as sg
from datetime import datetime, strptime

sg.theme('Black')

layout = [
    [sg.Text("Enter full name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
    [sg.Text("Enter your passport number:"), sg.Input(key='-PASSPORT_NUMBER-', do_not_clear=True, size=(10, 1))],
    [sg.Radio("Male", "RADIO", key='-MALE-'), sg.Radio("Female", "RADIO", key='-FEMALE-')],
    [sg.Input(key='-DEPARTURE-', size=(20, 1)), sg.CalendarButton("DATE OF DEPARTURE", close_when_date_chosen=True, target='-DEPARTURE-')],
    [sg.Input(key='-ARRIVAL-', size=(20, 1)), sg.CalendarButton("DATE OF ARRIVAL", close_when_date_chosen=True, target='-ARRIVAL-')],
    [sg.Text('Choose your destination:', size=(30, 1), font='Lucida', justification='left')],
    [sg.Listbox(values=['Havana', 'Moscow', 'Beijing', 'Tehran', 'Damascus', 'Tripoli', 'Sanaa'], size=(40, 5),
                      select_mode='single', default_values=['Havana'], key='-DESTINATION-')],
    [sg.Button('Reserve Ticket'), sg.Exit()]
]

window = sg.Window('привет Airlines', layout)


def validate(values):
    error_dict = {}

    if not values['-NAME-']:
        error_dict['-NAME-'] = 'Invalid: Name'

    if not values['-PASSPORT_NUMBER-'].isnumeric():
        error_dict['-PASSPORT_NUMBER-'] = 'Invalid: Passport Number'

    if not values['-MALE-'] and not values['-FEMALE-']:
        error_dict['-GENDER-'] = 'Invalid: Gender'

    if not values['-DEPARTURE-']:
        error_dict['-DEPARTURE-'] = 'Invalid: Departure Date'

    if not values['-ARRIVAL-']:
        error_dict['-ARRIVAL-'] = 'Invalid: Arrival Date'

    if '-DEPARTURE-' in values and '-ARRIVAL-' in values and \
            not is_arrival_before_departure(values['-DEPARTURE-'], values['-ARRIVAL-']):
        error_dict['-ARRIVAL-'] = 'Invalid: Arrival Date comes before Departure Date'

    if not values['-DESTINATION-']:
        error_dict['-DESTINATION-'] = 'Invalid: Destination'

    return not error_dict, error_dict


while (event := window.read()[0]) not in (sg.WIN_CLOSED, 'Exit'):
    if event == 'Reserve Ticket':
        is_valid, error_dict = validate(values)
        if is_valid:
            sg.popup('Flight Reservation submitted!')
        else:
            error_message = ''.join([f"\n{error_dict[key]}" for key in error_dict])
            sg.popup(error_message)

window.close()