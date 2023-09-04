import pyttsx3
import PySimpleGUI as psg

layout = [
    [psg.T('What do you want to say? ')],
    [psg.I(key='-SPEECH-')],
    [psg.B('SPEECH', key='-text-')]
]


def text_2_speech(text):
    engine = pyttsx3.init()

    engine.getProperty('rate')

    engine.setProperty('rate', 200)

    volume = engine.getProperty('volume')
    # print(f'Volume is {volume}')

    engine.setProperty('volume', 1)

    voices = engine.getProperty('voices')
    # print(f'Male voice: {voices[0].id}')
    # print(f'Female voice: {voices[1].id}')

    engine.setProperty('voice', voices[1].id)
    engine.say(v['-SPEECH-'])
    engine.runAndWait()


window = psg.Window('Text to Speech', layout)

while True:
    e, v = window.read()
    if e == psg.WIN_CLOSED:
        break
    if e == '-text-':
        text_2_speech('-text-')
window.close()