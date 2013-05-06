#! /usr/bin/env python

import random

class ant(object):
    ''' Ants looks for food, when they find it they return home follwing a
        random path. Leaving behind a trail of pheremones.

        Ants look randomly, unless they see a pheremone trail. If they see
        multiple trails they follow the strongest.
    '''
    def __init__(self, location):
        self.home = hive
        self.have_food = False
        self.location = location

    def look(self):
        pass

    def move(self, newLocation):
        self.location = newLocation

    def found_food(self):
        pass

    def return_home(self):
        pass

class world(object):
    ''' World contains the hive, the ants, and the food.
    '''
    def __init__(self, size, food='random', hive='random'):
        self.world = [[point]*size]*size
        if hive == 'random':
            hLocation = (random.randint(0,size), random.randint(0,size))
        else:
            hLocation = hive

        if food == 'random':
            fLocation = (random.randint(0,size), random.randint(0,size))
        else:
            fLocation = food

        self.create_hive(hLocation)
        self.create_food(fLocation)
        self.totalFood = self.point(fLocation).foodLeft

    def create_hive(self, hiveLocation):
        x, y = hiveLocation
        self.world[x][y] = hive(hiveLocation)

    def create_food(self, foodLocation, amount=100):
        x, y = foodLocation
        self.world[x][y] = food(foodLocation, amount)

    def show_world(self):
        return self.world

    def point(self, coords):
        x, y = coords
        return self.world[x][y]

class point(object):
    ''' A point in the world. This keeps track of the pheremone trails.
        or food, or hive.
    '''
    def __init__(self, location):
        self.location = location
        self.neighbours = []
        self.pheremones  = 0
    
    def pheremoneDecay(self):
        self.pheremones -= 1
    
    def pheremoneAdd(self):
        self.pheremones += 1

    def find_neighbours(self):
        self.neighbours.append(stuff)

class hive(point):
    ''' Hive object, keeps track of how much food is collected. So that we can
        figure out if we have reached the end of the simulation.
        
    '''
    def __init__(self, location):
        point.__init__(self, location)
        self.food = 0

    def addFood(self):
        self.food += 1

class food(point):
    ''' Food object. Keeps track of how much food is left. 
    '''
    def __init__(self, location, amount=100 ):
        point.__init__(self, location)
        self.foodLeft = amount

    def remove_food(self):
        self.foodLeft -= 1
