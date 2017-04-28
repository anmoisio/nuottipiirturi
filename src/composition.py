from note import Note
from rest import Rest

class Composition(object):
    
    def __init__(self, name, creator, meter, length):
        '''
        @param meter: beats per measure
        @param length: length of the melody in measures, integer
        '''
        self.notes  = []
        self.rests  = []
        self.beams  = []
        self.lyrics = []
        self.creator = creator
        self.name = name
        self.meter = meter
        self.length = length
        
        
        
    def add_note(self, note):
        for rest in self.rests:
            if rest.start == note.start and rest.measure == note.measure:
                self.remove_rest(rest.measure, rest.start)
        self.notes.append(note)
        
    def remove_note(self, measure, start, pitch):
        for note in self.notes:
            if measure == note.measure and note.start == start and pitch == note.pitch:
                self.notes.remove(note)

    def add_rest(self, rest):
        for old in self.rests:
            if rest.measure == old.measure:
                if rest.start == old.start:
                    self.remove_rest(old.measure, old.start)
                elif old.start < rest.start and (old.duration + old.start) > rest.start:
                    old.duration = rest.start - old.start
        self.rests.append(rest)
        
    def remove_rest(self, measure, start):
        for rest in self.rests:
            if measure == rest.measure and rest.start == start:
                self.rests.remove(rest)
        
    def add_beam(self,beam):
        self.beams.append(beam)
        
    def remove_beam(self, measure, start):
        for beam in self.beams:
            if measure == beam.measure and beam.start == start:
                self.beams.remove(beam)
        
    def fill_holes(self):
        ''' Fills empty beats with rests.'''
        
        for measure in range(self.length):
            shortest = 1
            for note in self.notes:                         # e.g. if shortest note is 1/8, measure contains 8 columns
                if measure == note.measure:                 #
                    if note.duration < shortest:            #
                        shortest = note.duration            #
                        
            for i in range(1, int(1/shortest) + 1):
                a = 0
                for note in self.notes:
                    if measure == note.measure:
                        if note.start == i*shortest:
                            a += 1
                        elif note.start < (i*shortest) and (note.start + note.duration) > (i*shortest):
                            a += 1
                for rest in self.rests:
                    if measure == rest.measure:
                        if rest.start == i*shortest:
                            a += 1
                        elif rest.start < (i*shortest) and (rest.start + rest.duration) > (i*shortest):
                            a += 1
                if a == 0:
                    rest = Rest(measure, i*shortest, shortest)       # (item_type, pitch, measure, start, duration)
                    self.add_rest(rest)
                        