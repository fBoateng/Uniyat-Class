'''import PySimpleGUI as sg

sg.change_look_and_feel('DarkBlue')


def change_theme(theme: str):
    if theme == 'Dark':
        sg.change_look_and_feel('Dark')
    elif theme == 'Light':
        sg.change_look_and_feel('LightGreen')
    else:
        sg.change_look_and_feel('DarkBlue')


layout = [[sg.Text('Fuel Purchasing App')],
          [sg.Text('Fuel type:'), sg.Combo(['Petrol', 'Diesel'], key='fuel_type')],
          [sg.Text('Quantity (Liters):'), sg.Input(key='quantity')],
          [sg.Text('Price per liter:'), sg.Input(key='price')],
          [sg.Text('Payment method:'), sg.Combo(['Cash', 'Card'], key='payment')],
          [sg.Text('Total Cost:'), sg.Text('', key='total_cost')],
          [sg.Button('Purchase'), sg.Button('Recent Purchases'), sg.Button('Cancel'),
           sg.Button('Change Theme', key='Change Theme', button_color=('black', 'white'), bind_return_key=True,
                     focus=True, enable_events=True)],
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
            sg.popup('Recent Purchases', '\n'.join(receipts))
        except:
            sg.popup('Error', 'No recent purchases')
    elif event == 'Change Theme':
        theme = sg.popup_get_text("please select the theme", "Change Theme")
        change_theme(theme)

window.close()'''
