import PySimpleGUI as sg

layout = [
    [sg.I(key='-NAME-')],
    [
        sg.ML(key='-IN-')
    ],
    [sg.Submit('Submit')],
    [sg.CloseButton('Close')],
    [sg.Sl(key='-sl-')],
    [sg.Spin(['chelsea', 'cardiff'], size=(15, 15), background_color='grey')]
]

window = sg.Window('New window', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        window['-IN-'].update(values['-NAME-'])

window.close()
