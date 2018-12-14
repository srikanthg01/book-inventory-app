from inventory import Inventory

order = {}

class User(Inventory): # why user is inherting from Book,
    # Inheritance is like
    # A is like B
    # then B(A) # this inhertiance is correnct
    def __init__(self, k):
        self.inventory = k

    def order_Book(self, name, copies):
        self.name = name
        self.copies = copies
        if self.copies == self.inventory[self.name]['copies']:
            self.inventory.pop(self.name)
            self._calc_order(name, copies)
        elif self.copies < self.inventory[self.name]['copies']:
            self.inventory[self.name]['copies'] = self.inventory[self.name]['copies'] - self.copies
            self._calc_order(name, copies)
        else:
            print "No sufficient stocks"

    def rating_Book(self, name, rating):
        self.name = name
        self.rating = rating
        if self.rating == 1:
            if 'ratings' not in self.inventory[self.name].keys():
                self.inventory[self.name]['ratings'] = {}
                self.inventory[self.name]['ratings']['5 Star'] = self.rating 
            else:
                self.inventory[self.name]['ratings']['5 Star'] = 1 + self.inventory[self.name]['ratings']['5 Star']
        if self.rating == 2:
            if 'ratings' not in self.inventory[self.name].keys():
                self.inventory[self.name]['ratings'] = {}
                self.inventory[self.name]['ratings']['4 Star'] = 1 
            else:
                self.inventory[self.name]['ratings']['4 Star'] = 1 + self.inventory[self.name]['ratings']['4 Star']
        if self.rating == 3:
            if 'ratings' not in self.inventory[self.name].keys():
                self.inventory[self.name]['ratings'] = {}
                self.inventory[self.name]['ratings']['3 Star'] = 1 
            else:
                self.inventory[self.name]['ratings']['3 Star'] = 1 + self.inventory[self.name]['ratings']['3 Star']
        if self.rating == 4:
            if 'ratings' not in self.inventory[self.name].keys():
                self.inventory[self.name]['ratings'] = {}
                self.inventory[self.name]['ratings']['2 Star'] = 1
            else:
                self.inventory[self.name]['ratings']['2 Star'] = 1 + self.inventory[self.name]['ratings']['2 Star']
        if self.rating == 5:
            if 'ratings' not in self.inventory[self.name].keys():
                self.inventory[self.name]['ratings'] = {}
                self.inventory[self.name]['ratings']['1 Star'] = 1
            else:
                self.inventory[self.name]['ratings']['1 Star'] = 1 + self.inventory[self.name]['ratings']['1 Star']

    def _calc_order(self, n, c):
        self.name = n
        self.copies = c
        if self.name not in order.keys():
            order[self.name] = self.copies
        else:
            order[self.name] = order[self.name] + self.copies

    def display_Order(self, name):
        self.name =  name
        print order[self.name]
