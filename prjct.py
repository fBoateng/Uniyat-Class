"""import PySimpleGUI as sg
import qrcode
import os
import PIL

layout = [
    [sg.T('Please enter your full name:'), sg.I(key='-name-', s=(20, 1), do_not_clear=True, pad=(35, 5))],
    [sg.T('Please enter your phone number:'), sg.I(key='-number-', s=(20, 1), do_not_clear=True, pad=(5, 10))],
    [sg.Radio('Male', "Radio", key='-male-'), sg.Radio('Female', "Radio", key='-female-')],
    [sg.I(key='-departure-', size=(25, 1)), sg.CalendarButton('Select Day Of Departure', close_when_date_chosen=True,
                                                              target='-departure-', location=(10, 10),
                                                              no_titlebar=False)],
    [sg.LB(values=['Accra', 'Kumasi', 'Cape Coast', 'Takoradi', 'Tamale', 'Ho', 'Koforidua'], size=(40, 5), pad=(5, 5),
           select_mode='single', key='-destination-')], [sg.T('QR IMAGE')],
    [sg.Image(key='-IMG-')],
    [sg.B('Reserve Ticket'), sg.B('Check Reservations'), sg.Exit()],

]


def inputformat(values):
    information = 'Ticket Booked!'
    name = '\nName: ' + values['-name-']
    information += name
    number = '\nNumber: ' + values['-number-']
    information += number
    gender = '\nGender: '
    if values['-male-']:
        gender += 'Male'
    else:
        gender += 'Female'
    departure_time = '\nDeparture Time: ' + values['-departure-']
    information += departure_time
    destination = '\nDestination: ' + values['-destination-'][0]
    information += destination

    return information








window = sg.Window('Test Reservation', layout)

while True:
    events, values = window.read()
    if events in (sg.WIN_CLOSED, 'Exit'):
        break
    elif events == 'Reserve Ticket':
        sg.Popup(inputformat(values))
        ticket_info = ''.join(inputformat(values))
        print(ticket_info)


window.close()"""



import PySimpleGUI as sg
import qrcode
import os

layout = [
    [sg.T('Please enter your full name:'), sg.I(key='-name-', s=(20, 1), do_not_clear=True, pad=(35, 5))],
    [sg.T('Please enter your phone number:'), sg.I(key='-number-', s=(20, 1), do_not_clear=True, pad=(5, 10))],
    [sg.Radio('Male', "Radio", key='-male-'), sg.Radio('Female', "Radio", key='-female-')],
    [sg.I(key='-departure-', size=(25, 1)), sg.CalendarButton('Select Day Of Departure', close_when_date_chosen=True,
                                                              target='-departure-', location=(10, 10),
                                                              no_titlebar=False)],
    [sg.LB(values=['Accra', 'Kumasi', 'Cape Coast', 'Takoradi', 'Tamale', 'Ho', 'Koforidua'], size=(40, 5), pad=(5, 5),
           select_mode='single', key='-destination-')], [sg.T('QR IMAGE')],
    [sg.Image(key='-IMG-')],
    [sg.B('Reserve Ticket'), sg.B('Check Reservations'), sg.Exit()],

]

def inputformat(values):
    information = f"Ticket Booked!\nName: {values['-name-']}\nNumber: {values['-number-']}\nGender: {values.get('-male-', 'Unknown')}\nDeparture Time: {values['-departure-']}\nDestination: {values['-destination-'][0]}"
    return information

window = sg.Window('Test Reservation', layout)
running = True

while running:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        running = False
    elif event == 'Reserve Ticket':
        ticket_info = inputformat(values)
        path = os.path.join(os.getcwd(), 'Qr.png')
        qr = qrcode.QRCode(
            box_size=5,
            border=5,
            version=1
        )
        qr.add_data(ticket_info)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(path)
        window['-IMG-'].update(filename=path)
        window.Layout()

window.close()
