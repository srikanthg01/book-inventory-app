from inventory import Inventory

class Author(object):

    def __init__(self, k):
        self.inventory = k

    def list_Book(self, author):
        self.author = author
        for k, v in self.inventory.iteritems():
            if self.inventory[k]['author'] == self.author:
                print k + "\n", 
