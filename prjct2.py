'''import PySimpleGUI as sg

sg.change_look_and_feel('DarkBlue')


def change_theme(theme: str):
    if theme == 'Dark':
        sg.change_look_and_feel('Dark')
    elif theme == 'Light':
        sg.change_look_and_feel('LightGreen')
    else:
        sg.change_look_and_feel('DarkBlue')


fuel_type_group = [
    [sg.Text('Fuel Type:', size=(12, 1)),
     sg.Combo(['Petrol', 'Diesel'], key='fuel_type', size=(10, 1))]
]

quantity_price_group = [
    [sg.Text('Quantity (Liters):', size=(15, 1)),
     sg.Input(key='quantity', size=(10, 1))],
    [sg.Text('Price per liter:', size=(15, 1)),
     sg.Input(key='price', size=(10, 1))]
]

payment_group = [
    [sg.Text('Payment Method:', size=(15, 1)),
     sg.Combo(['Cash', 'Card'], key='payment', size=(10, 1))]
]

total_cost_group = [
    [sg.Text('Total Cost:', size=(15, 1)),
     sg.Text('', key='total_cost', size=(10, 1))]
]

button_group = [
    [sg.Button('Purchase', button_color=('white', 'green'), size=(10, 1)),
     sg.Button('Recent Purchases', button_color=('white', 'blue'), size=(15, 1)),
     sg.Button('Cancel', button_color=('white', 'red'), size=(10, 1)),
     sg.Button('Change Theme', key='Change Theme', button_color=('black', 'white'), size=(12, 1),
               bind_return_key=True, focus=True, enable_events=True)]
]

layout = [[sg.Text('Fuel Purchasing App', font=('Arial', 20))],
          [sg.Column(fuel_type_group, element_justification='c'),
           sg.Column(quantity_price_group, element_justification='c')],
          [sg.Column(payment_group, element_justification='c')],
          [sg.Column(total_cost_group, element_justification='c')],
          [sg.HorizontalSeparator()],
          [sg.Column(button_group, element_justification='c')]]

window = sg.Window('Fuel Purchasing App', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    elif event == 'Purchase':
        fuel_type = values['fuel_type']
        quantity = values['quantity']
        price = values['price']
        payment = values['payment']

        if not fuel_type or not quantity or not price or not payment:
            sg.popup_error('Please fill in all fields')
            continue

        try:
            quantity = float(quantity)
            price = float(price)
        except ValueError:
            sg.popup_error('Quantity and price must be numbers')
            continue

        total_cost = quantity * price
        window['total_cost'].update(total_cost)

        elif event == 'Purchase':
        fuel_type = values['fuel_type']
        quantity = values['quantity']
        price = values['price']
        payment = values['payment']

        if not fuel_type or not quantity or not price or not payment:
            sg.popup_error('Please fill in all fields')
            continue

        try:
            quantity = float(quantity)
            price = float(price)
        except ValueError:
            sg.popup_error('Quantity and price must be numbers')
            continue

        total_cost = quantity * price
        window['total_cost'].update(total_cost)

        # Save receipt
        confirmation = sg.popup_yes_no('Do you want to save the receipt?', 'Save Receipt')
        if confirmation == 'Yes':
            receipt = {'Fuel Type': fuel_type, 'Quantity': quantity, 'Price': price, 'Payment Method': payment,
                       'Total Cost': total_cost}
            try:
                with open('receipts.txt', 'a') as f:
                    f.write(str(receipt) + '\n')
            except:
                sg.popup_error('Error saving receipt')'''







'''import PySimpleGUI as sg

# Constants
WINDOW_TITLE = 'Fuel Purchasing App'
THEMES = {'Dark': 'Dark', 'Light': 'LightGreen'}
FUEL_TYPES = ['Petrol', 'Diesel']
BUTTON_PURCHASE = 'Purchase'
BUTTON_RECENT_PURCHASES = 'Recent Purchases'
BUTTON_CANCEL = 'Cancel'
BUTTON_CHANGE_THEME = 'Change Theme'
LABEL_FUEL_TYPE = 'Fuel type:'
LABEL_QUANTITY = 'Quantity (Liters):'
LABEL_PRICE = 'Price per liter:'
LABEL_PAYMENT = 'Payment method:'
LABEL_TOTAL_COST = 'Total Cost:'
RECEIPTS_FILE = 'receipts.txt'


def change_theme_event(window):
    theme = window[BUTTON_CHANGE_THEME].get()
    sg.change_look_and_feel(THEMES[theme])


def purchase_event(window):
    try:
        fuel_type = window['fuel_type'].get()
        quantity = float(window['quantity'].get())
        price = float(window['price'].get())
        payment = window['payment'].get()
        total_cost = quantity * price
        window['total_cost'].update(total_cost)

        # Save receipt
        receipt = {'Fuel Type': fuel_type, 'Quantity': quantity, 'Price': price, 'Payment Method': payment,
                   'Total Cost': total_cost}
        with open(RECEIPTS_FILE, 'a') as f:
            f.write(str(receipt) + '\n')
    except Exception as e:
        sg.popup('Error', str(e))


def recent_purchases_event():
    try:
        with open(RECEIPTS_FILE, 'r') as f:
            receipts = f.readlines()
        sg.popup('Recent Purchases', '\n'.join(receipts))
    except:
        sg.popup('Error', 'No recent purchases')


def create_window():
    # Set window theme
    sg.change_look_and_feel('DarkBlue')

    # Set window layout
    layout = [[sg.Text('Fuel Purchasing App')],
              [sg.Text(LABEL_FUEL_TYPE), sg.Combo(FUEL_TYPES, key='fuel_type')],
              [sg.Text(LABEL_QUANTITY), sg.Input(key='quantity')],
              [sg.Text(LABEL_PRICE), sg.Input(key='price')],
              [sg.Text(LABEL_PAYMENT), sg.Combo(['Cash', 'Card'], key='payment')],
              [sg.Text(LABEL_TOTAL_COST), sg.Text('', key='total_cost')],
              [sg.Button(BUTTON_PURCHASE), sg.Button(BUTTON_RECENT_PURCHASES), sg.Button(BUTTON_CANCEL),
               sg.Button(BUTTON_CHANGE_THEME, button_color=('black', 'white'), bind_return_key=True,
                         focus=True, enable_events=True)],
              ]

    # Create window
    window = sg.Window(WINDOW_TITLE, layout)

    # Event loop
    while True:
        event, values = window.read()
        if event in (None, BUTTON_CANCEL):
            break
        elif event == BUTTON_PURCHASE:
            purchase_event(window)
        elif event == BUTTON_RECENT_PURCHASES:
            recent_purchases_event()
        elif event == BUTTON_CHANGE_THEME:
            change_theme_event(window)

    # Close window
    window.close()

if __name__ == '__main__':
    create_window()'''

import PySimpleGUI as sg

FUEL_TYPES = ['Petrol', 'Diesel']
THEMES = {'Dark': 'Dark', 'Light': 'LightGreen'}


def change_theme_event(window):
    theme = window['Change Theme'].metadata
    sg.change_look_and_feel(THEMES[theme])


def create_window():
    layout = [[sg.Text('Fuel Purchasing App', font='Any 15')],
              [sg.Text('Fuel type:', font='Any 12'), sg.Combo(FUEL_TYPES, key='fuel_type', font='Any 12')],
              [sg.Text('Quantity (Liters):', font='Any 12'), sg.Input(key='quantity', font='Any 12')],
              [sg.Text('Price per liter:', font='Any 12'), sg.Input(key='price', font='Any 12')],
              [sg.Text('Payment method:', font='Any 12'), sg.Combo(['Cash', 'Card'], key='payment', font='Any 12')],
              [sg.Text('Total Cost:', font='Any 12'), sg.Text('', key='total_cost', font='Any 12')],
              [sg.Button('Purchase', font='Any 12'), sg.Button('Recent Purchases', font='Any 12'),
               sg.Button('Cancel', font='Any 12')],
               #sg.Button('Change Theme', key='Change Theme', button_color=('black', 'white'), font='Any 12',
                         #bind_return_key=True, focus=True, enable_events=True)],
              #sg.Button(theme, key='Change Theme', metadata=theme) for theme in THEMES]

              ]

    window = sg.Window('Fuel Purchasing App', layout)

    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        elif event == 'Purchase':
            fuel_type = values['fuel_type']
            quantity = float(values['quantity'])
            price = float(values['price'])
            payment = values['payment']
            total_cost = quantity * price
            window['total_cost'].update(total_cost)

            # Save receipt
            receipt = {'Fuel Type': fuel_type, 'Quantity': quantity, 'Price': price, 'Payment Method': payment,
                       'Total Cost': total_cost}
            with open('receipts.txt', 'a') as f:
                f.write(str(receipt) + '\n')
        elif event == 'Recent Purchases':
            try:
                with open('receipts.txt', 'r') as f:
                    receipts = f.readlines()
                sg.popup('Recent Purchases', '\n'.join(receipts), font='Any 12')
            except:
                sg.popup('Error', 'No recent purchases', font='Any 12')
        elif event == 'Change Theme':
            change_theme_event(window)

    window.close()


if __name__ == '__main__':
    sg.theme('DarkBlue')
    create_window()
