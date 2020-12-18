import pretty_midi
import random

class ZBass:
    def __init__(self, key, tempo, fileName):
        keyArray = self.getKey(key)
        self.tempo = tempo
        numberOfBeats = 60
        beatLength = 1

        instrument = self.create(keyArray, numberOfBeats, beatLength)
        self.createFile(instrument, fileName)
        return

    def getKey(self, key):
        #key = ['D2', 'E2', 'F#2', 'G2', 'A2', 'B2', 'C#3','D3']
        #key = ['D2', 'G2', 'A2', 'D3']
        key = ['D2', 'E2', 'F#2', 'G2', 'A2', 'B2', 'C#3','D3', 'E3', 'F#3', 'G3', 'A3', 'B3', 'C#4', 'D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5', 'D5', 'E5', 'F#5', 'G5', 'A5', 'B5', 'C#6', 'D6']
        return key

    def create(self, keyArray, numberOfBeats, beatLength):
        place = 0
        noteIsDifferent = False
        previousNote = -1
        cello_program = pretty_midi.instrument_name_to_program('Cello')
        instrument = pretty_midi.Instrument(program=cello_program)
        measure = []

        while place <= 4:
            lengthOfNote = self.getLengthOfNote(beatLength, place)
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
            measure.append(note)
            place = place + lengthOfNote
            noteIsDifferent = False
            previousNote = pitch

        while place < 61:
            for each in range(0, len(measure) - 1):
                instrument.notes.append(measure[each])
            place = place + 4

        return instrument

    def getLengthOfNote(self, beatLength, place):
        #lengths = [.5, 1, 2] 
        lengths = [.5, 1] 
        length = lengths[random.randint(0, 1)]
        if length + place > 5:
            length = 5 - place
        return length * beatLength

    def createFile(self, instrument, fileName):
        self.pm = pretty_midi.PrettyMIDI()
        self.pm.instruments.append(instrument)
        self.pm.write(fileName)
        return

#################################################

#creates a one measure pattern to be repeated, full range

number = '10'

#z = ZBass('D', 120, 'ostinatoOutput ' + number + '.1.mid')
#z = ZBass('D', 120, 'ostinatoOutput ' + number + '.2.mid')
#z = ZBass('D', 120, 'ostinatoOutput ' + number + '.3.mid')
#z = ZBass('D', 120, 'ostinatoOutput ' + number + '.4.mid')

z = ZBass('D', 120, 'ostinatoOutput.mid')
