import mido
from os import path


def extract_pitches(filename):
    try:
        midi = mido.MidiFile(path.dirname(__file__) +
                             "/training data/midi/" + filename)
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt: ", filename)
        midi = ""
    pitches = []

    for message in midi:
        if message.type == 'note_on':
            pitches.append(int(message.note)-55)
    return pitches


def write_midi_file(filename, notes, tempo=500000):
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)

    track.append(mido.MetaMessage('set_tempo', tempo=tempo))

    for note in notes:
        track.append(mido.Message(
            'note_on', note=note+55, velocity=94, time=0))
        track.append(mido.Message(
            'note_off', note=note+55, velocity=94, time=480))

    mid.save(path.dirname(__file__) + "/new_tunes/" + filename)
