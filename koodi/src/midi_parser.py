import mido
from os import path


def extract_pitches(filename):
    midi = mido.MidiFile(path.dirname(__file__) +
                         "/training data/midi/" + filename)
    pitches = []

    for message in midi:
        if message.type == 'note_on':
            pitches.append(int(message.note)-55)
    return pitches
