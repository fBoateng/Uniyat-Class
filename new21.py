import PySimpleGUI as sg

FUEL_TYPES = ['Petrol', 'Diesel']
THEMES = {'Dark': 'Dark', 'Light': 'LightGreen'}


def change_theme_event(window):
    theme = window['Change Theme'].metadata
    sg.change_look_and_feel(THEMES[theme])


def create_window():
    layout = [[sg.Text('Fuel Purchasing App', font='Any 15')],
              [sg.Text('Fuel type:', font='Any 12'), sg.Combo(FUEL_TYPES, key='fuel_type')],
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
