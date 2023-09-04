import PySimpleGUI as psg
import qrcode
import os
import PIL
from datetime import datetime, date
import string

psg.theme('LightGreen')

col_a = [
    [psg.T('QR IMAGE')],
    [psg.Image(key='-IMG-')],
]

layout = [
    [psg.T('Please enter your full name:'), psg.I(key='-name-', s=(20, 1), do_not_clear=True, pad=(35, 5))],
    [psg.T('Please enter your phone number:'), psg.I(key='-number-', s=(20, 1), do_not_clear=True, pad=(5, 10))],
    [psg.Radio('Male', "Radio", key='-male-'), psg.Radio('Female', "Radio", key='-female-')],
    [psg.I(key='-departure-', size=(25, 1)), psg.CalendarButton('Select Day Of Departure', close_when_date_chosen=True,
                                                                target='-departure-', location=(10, 10),
                                                                no_titlebar=False)],
    [psg.LB(values=['Accra', 'Kumasi', 'Cape Coast', 'Takoradi', 'Tamale', 'Ho', 'Koforidua'], size=(40, 5), pad=(5, 5),
            select_mode='single', key='-destination-')],
    [psg.B('Reserve Ticket'), psg.B('Check Reservations'), psg.Exit()],
    [psg.HSep()], [psg.Col(col_a)]

]

reservations = []


def is_today_before_departure(departure_string):
    # 2021-08-01 13:09:43
    departure_object = datetime.strptime(departure_string, '%Y-%m-%d %H:%M:%S')
    today_string = date.today()
    return today_string < departure_object


window = psg.Window('Bay Transports', layout)


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


def reservation_list(values, reservations):
    receipt = f"Reservation details:\n{inputformat(values)}\n"
    with open('receipt.txt', 'a') as f:
        f.write(receipt)
    return reservations.append(inputformat(values))


def qrcode_gen(ticket_info):
    qr = qrcode.QRCode(
        box_size=5,
        border=5,
        version=1
    )
    qr.add_data(ticket_info)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    file_name = 'Qr' + '.png'
    path = os.path.join(os.getcwd(), file_name)
    img.save(path)
    return path


def generate_error_message(values_invalid):
    error_message = 'The following fields are invalid: '
    for value in values_invalid:
        error_message += value + ', '
    error_message = error_message[:-2]
    return error_message


def validate(values):
    is_valid = True
    values_invalid = []

    if len(values['-name-']) == 0:
        values_invalid.append('Name')
        is_valid = False

    if not values['-number-'].isnumeric():
        values_invalid.append('Number')
        is_valid = False

    if not values['-male-'] and not values['-female-']:
        values_invalid.append('Gender')
        is_valid = False

    return is_valid


'''def validate(values):
    is_valid = True
    values_invalid = []

    if len(values['-name-']) == 0:
        values_invalid.append('Name')
        is_valid = False

    if not values['-number-'].isnumeric():
        values_invalid.append('Number')
        is_valid = False

    if not values['-male-'] and not values['-female-']:
        values_invalid.append('Gender')
        is_valid = False

    if not is_valid:
        error_message = generate_error_message(values_invalid)
        psg.popup(error_message)

    return is_valid, values_invalid'''

'''def validate(values):
    is_valid = True
    values_invalid = []

    if len(values['-name-']) == 0:
        values_invalid.append('Name')
        is_valid = False

    if not values['-number-'].isnumeric():
        values_invalid.append('Number')
        is_valid = False

    if not values['-male-'] and not values['-female-']:
        values_invalid.append('Gender')
        is_valid = False'''


def validate(values):
    # validate the input values
    invalid_values = []
    for key, value in values.items():
        if key == '-departure-':
            try:
                datetime.datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                invalid_values.append(key)
       # elif key == 'Flight Time':
        #    try:
         #       datetime.datetime.strptime(value, '%H:%M')
            except ValueError:
                invalid_values.append(key)
        elif not value:
            invalid_values.append(key)

    if len(invalid_values) > 0:
        return False, invalid_values
    else:
        return True, []


while True:
    event, values = window.read()
    if event in (psg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Reserve Ticket':
        validation_result = validate(values)
        if validation_result and validation_result[0]:
            reservation_list(values, reservations)
            psg.popup(inputformat(values))
            ticket_info = inputformat(values)
            qr_image_path = qrcode_gen(ticket_info)
            window['-IMG-'].update(filename=qr_image_path)
            psg.popup('Flight reservation submitted!')
        else:
            error_message = generate_error_message(validation_result[1])
            psg.popup(error_message)

    elif event == 'Check Reservations':
        if len(reservations) > 0:
            reservation_string = '\n'.join(reservations)
            psg.popup(reservation_string)
        else:
            psg.popup('No reservations have been made yet.')
    else:
        psg.popup('Unknown event received:', event)

window.close()
