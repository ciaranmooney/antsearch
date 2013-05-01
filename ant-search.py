#! /usr/bin/env python

class ant(object):
    ''' Ants looks for food, when they find it they return home by the most
        direct path. Leaving behind a trail of pheremones.

        Ants look randomly, unless they see a pheremone trail. If they see
        multiple trails they follow the strongest.
    '''
    def __init__(self, hive, location):
        self.home = hive
        self.have_food = False
        self.location = location

    def look(self):
        pass

    def move(self):
        pass

    def found_food(self):
        pass

    def return_home(self):
        pass

class world(object):
    ''' World contains the hive, the ants, and the food.
    '''
    def __init__(self, size, food='random', hive='random'):
        pass

    def create_hive(self):
        pass

    def create_food(self):
        pass

    def show_world(self):
        pass

class point(object):
    ''' A point in the world. This keeps track of the pheremone trails.
        or food, or hive.
    '''
    def __init__(self):
        self.pheremones  = 0
    
    def pheremone_decay(self):
        self.pheremones -= 1
