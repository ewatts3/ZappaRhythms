import pretty_midi
import random

class ZMelody:
    def __init__(self, key, tempo):
        self.key = self.getKey(key)
        self.tempo = tempo
        numberOfBeats = 60
        beatLength = 1

        instrument = self.create(self.key, numberOfBeats, beatLength)
        self.createFile(instrument)
        return

    def getKey(self, key):
        key = ['D2', 'E2', 'F#2', 'G2', 'A2', 'B2', 'C#3','D3', 'E3', 'F#3', 'G3', 'A3', 'B3', 'C#4', 'D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5', 'D5', 'E5', 'F#5', 'G5', 'A5', 'B5', 'C#6', 'D6']
        return key

    def create(self, key, numberOfBeats, beatLength):
        place = 0
        previousNote = 15
        cello_program = pretty_midi.instrument_name_to_program('Cello')
        instrument = pretty_midi.Instrument(program=cello_program)

        for each in range(1, numberOfBeats):
            numberOfNotesPerBeat = self.getNumberOfNotesPerBeat()
            if numberOfNotesPerBeat == 1:
                lengthOfNote = self.getRhythm(beatLength, numberOfNotesPerBeat)
                pitch = self.getPitch(key, previousNote)
                note = pretty_midi.Note(velocity=100,
                                        pitch=pretty_midi.note_name_to_number(key[pitch]),
                                        start=place,
                                        end=place + lengthOfNote)
                instrument.notes.append(note)
                place = place + lengthOfNote
            else:
                lengthOfNote = self.getRhythm(beatLength, numberOfNotesPerBeat)
                for each in range(0, numberOfNotesPerBeat):
                    pitch = self.getPitch(key, previousNote)
                    note = pretty_midi.Note(velocity=100,
                                            pitch=pretty_midi.note_name_to_number(key[pitch]),
                                            start=place,
                                            end=place + lengthOfNote)
                    instrument.notes.append(note)
                    place = place + lengthOfNote

        return instrument

    def getNumberOfNotesPerBeat(self):
        return random.randint(1, 7)

    def getRhythm(self, beatLength, numberOfNotesPerBeat):
        return (beatLength / numberOfNotesPerBeat)

    def getPitch(self, key, previousNote):
        validPitch = False

        while validPitch is False:
            interval = random.randint(0, 9) #Set 1: same note, set 2: 2nd or 3rd, set 3: 4th or 5th or 6th, set 4: 7th or 8th
            direction = random.randint(0, 1) #0 is down, 1 is up

            if interval < 3:
                pitch = previousNote
            elif interval > 2 and interval < 6:
                size = random.randint(0, 1) #0 is 2nd, 1 is 3rd
                if size == 0:
                    if direction == 0:
                        pitch = previousNote - 1
                    elif direction == 1:
                        pitch = previousNote + 1
                elif size == 1:
                    if direction == 0:
                        pitch = previousNote - 2
                    elif direction == 1:
                        pitch = previousNote + 2
            elif interval > 5 and interval < 9:
                size = random.randint(0, 2) #0 is 4th, 1 is 5th, 2 is 6th
                if size == 0:
                    if direction == 0:
                        pitch = previousNote - 3
                    elif direction == 1:
                        pitch = previousNote + 3
                elif size == 1:
                    if direction == 0:
                        pitch = previousNote - 4
                    elif direction == 1:
                        pitch = previousNote + 4
                elif size == 2:
                    if direction == 0:
                        pitch = previousNote - 5
                    elif direction == 1:
                        pitch = previousNote + 5
            elif interval == 9:
                size = random.randint(0, 1) #0 is 7th, 1 is 8th
                if size == 0:
                    if direction == 0:
                        pitch = previousNote - 6
                    elif direction == 1:
                        pitch = previousNote + 6
                elif size == 1:
                    if direction == 0:
                        pitch = previousNote - 7
                    elif direction == 1:
                        pitch = previousNote + 7

            if pitch < 0 or pitch > len(key):
                validPitch = False
            else:
                validPitch = True

        return pitch

    def createFile(self, instrument):
        self.pm = pretty_midi.PrettyMIDI()
        self.pm.instruments.append(instrument)
        self.pm.write('melodyOutput.mid')
        return

#################################################

#creates a melody from a full range where the number of notes for each beat is different
#The next note is dependent on the note that came before it

z = ZMelody('D', 120)
