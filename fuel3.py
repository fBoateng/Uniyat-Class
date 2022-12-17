import PySimpleGUI as sg
import qrcode
import os

sg.theme('SandyBeach')

col_a = [
    [sg.T('Enter Amount')],
    [sg.T('Please enter the amount you are purchasing? ')],
    [sg.T('Petrol: '), sg.I(k='-Input-', size=(15, 15), enable_events=True), sg.Submit('Submit', k='-Submit-')],
    [sg.T('Unit: '), sg.B('Litre', k='-Litre-', enable_events=True, button_color=('white', 'firebrick4'), p=10),
     sg.B('Gallon', k='-Gallon-', enable_events=True, button_color=('white', 'firebrick4'), p=10),
     sg.CloseButton('Close', p=15)],
    [sg.T('Output', key='-OUT-')]

]

col_b = [
    [sg.T('Petrol')],
    [sg.I(k='-IN-', size=15)],
    [sg.Spin(['litre to gallon', 'gallon to litre'], key='-UNIT-')],
    [sg.Button('Convert', key='-CONVERT-')],
    [sg.T('Output', key='-OUTPUT-')]
]

col_c = [
    [sg.T('Diesel')],
    [sg.I(k='-IN-', size=15)],
    [sg.Spin(['litre to gallon', 'gallon to litre'], key='-UNIT-')],
    [sg.Button('Convert', key='-CONVERT-')],
    [sg.T('Output', key='-OUTPUT-')]
]

col_d = [
    [sg.T('QR IMAGE')],

]


def qrcode_gen(link):
    qr = qrcode.QRCode(
        box_size=5,
        border=5,
        version=1
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='grey')
    file_name = 'Qr' + '.png'
    path = os.path.join(os.getcwd(), file_name)
    img.save(path)


layout = [
    [sg.Col(col_d)], [sg.HSep()],
    [sg.Col(col_a), sg.VSep(), sg.Col(col_b), sg.VSep(), sg.Col(col_c),
     ]
]

window = sg.Window('Buy Fuel', layout)
while True:
    e, v = window.read()
    if e == sg.WIN_CLOSED:
        break
    if e == '-Submit-':
        user_input = v['-Input-']
        if user_input.isnumeric():

            if user_input.isnumeric():
                sg.popup(f'You entered {user_input} cedis !')

window.close()
