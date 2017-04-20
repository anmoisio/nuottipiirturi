from composition import Composition
from item import Item

class Column(object):

    head_whole_odd          = "  ()  "
    head_whole_even         = "--()--"
    halfnote_odd            = "  OO  "
    halfnote_even           = "--OO--"
    head_odd                = "  @@  "
    head_even               = "--@@--"
    
    stem_odd                = "   |  "
    stem_even               = "---|--"
    
    eighth_stem1_even       = "   |\ "
    eighth_stem1_odd        = "---|\-"
    eighth_stem2_even       = "   \  "
    eighth_stem2_odd        = "---\--"
    
    s_stem_odd              = "   || "
    s_stem_even             = "---||-"


    beam                    = "======"
    beamstart_odd           = "   ==="
    beamstart_even          = "---==="
    beamend_odd             = "===   "
    beamend_even            = "===---"
    
    def __init__(self, items, measure, start):
        self.measure = measure                          # 0,1,2,...
        self.start = start                              # e.g. 1/8 - 8/8, moment in measure
        self.notes = []                                 # notes that start in this column
        self.beams = []
        self.rests = []               
        self.find_items(items)
        self.rows = 14 * [None]                         # 11 strings of 3 characters, the 11 rows of the stave
        self.add_rows()                                 # empty rows
        self.add_items()

        
    def add_rows(self):
        ''' Adds empty rows for this column. '''
        
        for i in range(0,14):
            self.rows[i] = "      "
        for i in range(2,11,2):
            self.rows[i] = "------"
        

    def find_items(self, items):
        ''' Finds items that are on this column. '''

        # items that start at this column
        for item in items:
            if item != None and item.measure == self.measure and item.start == self.start:
                self.notes.append(item)
                
        # implement: find beams over the column

                
    def add_items(self):
        '''
        Adds graphic items in the character list 'rows'
        according to 'notes' and other stuff ...
        '''
        
        if len(self.notes) == 1 and len(self.beams) == 0:
            note = self.notes[0]
                
            if note.pitch > 5:
                a = 1                                   # stem points up
            else:
                a = -1                                    # stem points down
                self.eighth_stem2_even = "   /  "
                self.eighth_stem2_odd = "---/--"
                self.eighth_stem1_even = "   |/ "
                self.eighth_stem1_odd = "---|/-"
                self.head_odd  = "   @@ "
                self.head_even = "---@@-"
                    
            if note.pitch % 2 == 0:          # note is on even row
                head = self.head_even
                head_half = self.halfnote_even
                head_whole = self.head_whole_even
                stem1 = self.stem_odd
                stem2 = self.stem_even
                e_stem1 = self.eighth_stem1_odd
                e_stem2 = self.eighth_stem1_even
                e_stem = self.eighth_stem2_odd
                s_stem = self.s_stem_odd
                
            else:                                         # note is on odd row
                head = self.head_odd
                head_half = self.halfnote_odd
                head_whole = self.head_whole_odd
                stem1 = self.stem_even
                stem2 = self.stem_odd
                e_stem1 = self.eighth_stem1_even
                e_stem2 = self.eighth_stem1_odd
                e_stem = self.eighth_stem2_even
                s_stem = self.s_stem_even
            
            if note.duration == 1:
                self.rows[note.pitch]           = head_whole
            
            elif note.duration == 1/2:
                self.rows[note.pitch]           = head_half
                self.rows[note.pitch - (1*a)]   = stem1
            
            elif note.duration == 1/4 or note.duration == 1/8 or note.duration == 1/16:
                self.rows[note.pitch]           = head
                self.rows[note.pitch - (1*a)]   = stem1

            if note.duration == 1/2 or note.duration == 1/4:
                self.rows[note.pitch - (2*a)]   = stem2
                self.rows[note.pitch - (3*a)]   = stem1
                self.rows[note.pitch - (4*a)]   = stem2
           
            elif note.duration == 1/8 or note.duration == 1/16:
                self.rows[note.pitch - (2*a)]   = e_stem1
                self.rows[note.pitch - (3*a)]   = e_stem2
                self.rows[note.pitch - (4*a)]   = e_stem
            
            if note.duration == 1/16:
                self.rows[note.pitch - (1*a)]   = s_stem
       
        elif len(self.notes) > 1 and len(self.beams) == 0:

            for i in range(len(self.notes) - 1):
                if self.notes[i].duration == self.notes[i+1].duration:
                    asd = True
                else: asd = False
            
            if asd:
                
                for i in range(len(self.notes) - 1):                         # sorting the list from lowest pitch to highest
                    for i in range(len(self.notes) - 1):               
                        if self.notes[i].pitch > self.notes[i+1].pitch:
                            print("j")
                            temp = self.notes[i]
                            self.notes[i] = self.notes[i+1]
                            self.notes[i+1] = temp
                            

                        
                highest = self.notes[0].pitch
                lowest = self.notes[len(self.notes)-1].pitch
                
                if highest > 5:
                    a = 1                                           # stem points up
                else:
                    a = -1                                            # stem points down
                    self.eighth_stem2_even = "  / "
                    self.eighth_stem2_odd = "--/-"
                    self.eighth_stem1_even = "  |/"
                    self.eighth_stem1_odd = "--|/"
                
                for i in range(len(self.notes)):    
                    if highest % 2 == 0:                     # note is on even row
                        head = self.head_even
                        stem1 = self.stem_odd
                        stem2 = self.stem_even
                        e_stem1 = self.eighth_stem1_odd
                        e_stem2 = self.eighth_stem1_even
                        e_stem = self.eighth_stem2_odd
                        #halfnote = self.halfnote_even            add all other types
                        
                    else:                                                 # note is on odd row
                        head = self.head_odd    
                        stem1 = self.stem_even
                        stem2 = self.stem_odd
                        e_stem1 = self.eighth_stem1_even
                        e_stem2 = self.eighth_stem1_odd
                        e_stem = self.eighth_stem2_even
                        
                    self.rows[self.notes[i].pitch] = head
                    dfg = 0
                    for j in range(highest,lowest):
                        for note in self.notes:
                            if note.pitch == j: dfg += 1
                            else: dfg = 0
                        if dfg == 0:
                            self.rows[j] = stem1
                    
                   
                if self.notes[i].duration == 1/4:
                    self.rows[self.notes[i].pitch - (1*a)]   = stem1
                    self.rows[self.notes[i].pitch - (2*a)]   = stem2
                    self.rows[self.notes[i].pitch - (3*a)]   = stem1
                    self.rows[self.notes[i].pitch - (4*a)]   = stem2
               
                elif self.notes[i].duration == 1/8:
                    self.rows[highest - (1*a)]   = stem1
                    self.rows[highest - (2*a)]   = e_stem1
                    self.rows[highest - (3*a)]   = e_stem2
                    self.rows[highest - (4*a)]   = e_stem
    