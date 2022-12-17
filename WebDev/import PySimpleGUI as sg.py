import PySimpleGUI as sg

layout = [
    [sg.Text('New Text')],
    [sg.Input('-Input-', font= 'times 20')],
    [sg.ML(size= (20, 25))],
    [sg.Spin(['Fish','Eggs', 'Meat'],font= 'times 20')]
]


window = sg.Window('test', layout).read()


window.close()