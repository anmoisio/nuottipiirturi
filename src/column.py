from composition import Composition
from item import Item

class Column(object):

    wholenote = "  ()"
    halfnote = " 00"
    quarternote_odd = " @@"
    quarternote_even = "-@@"
    eigthnote_odd = " oo"
    eigthnote_even = "-oo"
    stem_odd = "  |"
    stem_even = "--|"
    bar = "==="
    
    def __init__(self, composition, measure, start):
        self.measure = measure                            # 0,1,2,...
        self.start = start               # 1/8 - 8/8
        self.starting = 10 * [None]       # not ideal type of list ? the items that start in this column                   
        self.find_items(composition)
        self.rows = 11 * [None]                    # 11 strings of 3 characters, the 11 rows of the stave
        self.add_rows()                                   # empty rows
        self.add_items()

        
        
    def add_rows(self):
        ''' Adds empty rows for this column. '''
        
        for i in range(0,10,2):
            self.rows[i] = "---"
        for i in range(1,11,2):
            self.rows[i] = "   "
        self.rows[10] = "   "
        

    def find_items(self, composition):
        ''' Finds items that are on this column. '''

        # items that start at this column
        k = 0
        for i in range(len(composition.array)):
            
            if composition.array[i] != None and composition.array[i].measure == self.measure and composition.array[i].start == self.start:
                self.starting[k] = composition.array[i]
                print(self.starting[0])
                k += 1
                
        # implement: find bars over the column

                
    def add_items(self):
        '''
        Adds graphic items in the character list 'rows'
        according to 'starting' items and other stuff ...
        '''
        
        # starting list
        for i in range(len(self.starting)):
            if self.starting[i] != None and self.starting[i].item_type == Item.NOTE:
                if self.starting[i].duration == 1/4:
                    self.rows[self.starting[i].pitch]       = self.quarternote_odd
                    self.rows[self.starting[i].pitch - 1]   = self.stem_even
                    self.rows[self.starting[i].pitch - 2]   = self.stem_odd
                
                
        #### test print
        for i in range(len(self.rows)):
            print(self.rows[i])
        ####
    