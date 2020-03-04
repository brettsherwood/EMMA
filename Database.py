import csv

class Database():
    def scanDatabase(self, upc):
        READFILE = open('UPCList.csv', 'r')     #opens file to be read
        upclist = csv.reader(READFILE)
        
        for row in upclist:         #searches every row for matching barcode
            if str(upc) == str(row[0]):
                material = row[1]       #pulls recycling info from database
                recycle = row[2]        #and sets to variables
                rinse = row[3]

                READFILE.close()        #close file to not cause errors
                
                recycle_rinse = self.checkRecycleRinse(recycle,rinse)
                return (str(material), recycle_rinse)

        # if item is not found at all, return not found and an empty tuple
        return ('Not Found', ('', ''))
    

        

    def checkRecycleRinse(self, recycle, rinse):
        if recycle.upper() == 'YES':      #checks if item is recyclable
            if rinse.upper() == 'YES':    #checks if item needs to be rinsed
                return ('Recyclable!', 'Item should be rinsed out!')
            else:
                return ('Recyclable!', 'Item should not be rinsed!')
        else:
            return ('Not Recyclable :(', '')    #returns empty string to not casue error
            #non-recyclable items don't need to be rinsed

    
