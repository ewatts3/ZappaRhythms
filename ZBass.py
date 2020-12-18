import pretty_midi
import random

class ZBass:
    def __init__(self, key, tempo):
        keyArray = self.getKey(key)
        self.tempo = tempo
        numberOfBeats = 60
        beatLength = 1

        instrument = self.create(keyArray, numberOfBeats, beatLength)
        self.createFile(instrument)
        return

    def getKey(self, key):
        #key = ['D2', 'E2', 'F#2', 'G2', 'A2', 'B2', 'C#3','D3']
        key = ['D2', 'G2', 'A2', 'D3']
        return key

    def create(self, keyArray, numberOfBeats, beatLength):
        place = 0
        noteIsDifferent = False
        previousNote = -1
        cello_program = pretty_midi.instrument_name_to_program('Cello')
        instrument = pretty_midi.Instrument(program=cello_program)

        while place < 60:
            lengthOfNote = self.getLengthOfNote(beatLength)
            while noteIsDifferent is False:
                pitch = random.randint(0, len(keyArray) - 1)
                if pitch == previousNote:
                    noteIsDifferent = False
                else:
                   noteIsDifferent = True
            note = pretty_midi.Note(velocity=100,
                                    pitch=pretty_midi.note_name_to_number(keyArray[pitch]),
                                    start=place,
                                    end=place + lengthOfNote)
            instrument.notes.append(note)
            place = place + lengthOfNote
            noteIsDifferent = False
            previousNote = pitch

        return instrument

    def getLengthOfNote(self, beatLength):
        lengths = [.5, 1, 2] #2 default
        length = lengths[random.randint(0, 2)]
        return length * beatLength

    def createFile(self, instrument):
        self.pm = pretty_midi.PrettyMIDI()
        self.pm.instruments.append(instrument)
        self.pm.write('bassOutput.mid')
        return

#################################################

#randomly selects 1/4/5 scale degrees from a limited range to play for random lengths

z = ZBass('D', 120)
