class Inventory(object):
    # Why this is commented
    def __init__(self, k): 
        self.inventory = k
    
    def add_Book(self, name, copies): # use under score case in method names
        self.name = name
        self.copies = copies
        if self.name not in self.inventory.keys():
            price=input("Enter the price of the book: ")
            author=input("Enter the author of the book: ")
            self.inventory[self.name] = {'author': author, 'price': price, 'copies': self.copies}
        else:
            self.inventory[self.name]['copies'] = self.inventory[self.name]['copies'] + self.copies
        #print inventory

    def disp_Invent(self):
        print self.inventory
