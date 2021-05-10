import collections
from midiutil import MIDIFile

generated_folder = 'data/generated/'

vowels = set("AEIOUaeiou")
lyrics_vowels = []

track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 120   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

encoder = {
    'a' : 60,
    'e' : 62,    
    'i' : 63,
    'o' : 65,
    'u' : 67,
    'A' : 68,
    'E' : 70,
    'I' : 72,
    'O' : 74,
    'U' : 75,
}

def get_midi_from_vowels(filename):
    midiname = filename.split('.')[0] + '.mid'
    lyrics_vowels = []
    with open(filename, 'r') as file:
        lyrics = file.read().replace('\n', '')
    degrees = [encoder[letter] for letter in lyrics if letter in vowels]
    create_save_midi(midiname,  degrees, generated_folder)

def create_save_midi(midiname, degrees, output_dir):
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
    MyMIDI.addTempo(track, time, tempo)

    for i, pitch in enumerate(degrees):
        MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

    with open(str(output_dir + midiname), "wb") as output_file:
        MyMIDI.writeFile(output_file)