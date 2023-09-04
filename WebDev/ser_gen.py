import PySimpleGUI as sg
import random
import string


def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def create_pysimplegui_window():
    sg.theme('DarkBlue')

    layout = [[sg.Text('Serial Code Generator', font=('Helvetica', 16), justification='center')],
              [sg.Text('Click "Generate" to get your serial code:', font=('Helvetica', 12))],
              [sg.Text('', size=(20, 1), key='-OUTPUT-', font=('Helvetica', 14), justification='center')],
              [sg.Button('Generate', font=('Helvetica', 12)), sg.Button('Exit', font=('Helvetica', 12))]]

    window = sg.Window('Serial Code Generator', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Generate':
            code = generate_code()
            window['-OUTPUT-'].update(code)

    window.close()


if __name__ == '__main__':
    create_pysimplegui_window()
