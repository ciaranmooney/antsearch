#! /usr/bin/env python

import random
from random import choice

class ant(object):
    ''' Ants looks for food, when they find it they return home follwing a
        random path. Leaving behind a trail of pheremones.

        Ants look randomly, unless they see a pheremone trail. If they see
        multiple trails they follow the strongest.
    '''
    def __init__(self, hive):
        self.hive = hive.location
        self.have_food = False
        self.location = self.hive
        self.objective = "food"

    def look(self):
        ''' Check curent area for pheremones, food or hive.
        '''

    def move(self, newLocation):
        ''' Move to new location
        '''
        self.neighbours = self.hive.findNeighbours(self.location) 
        
        if self.lastPoint in self.neighbours:
            self.neighbours.remove(self.lastPoint)
        
        self.location = choice(self.neighbours)

    def foundFood(self):
        pass

    def returnHome(self):
        pass

class world(object):
    ''' World contains the hive, the pheremones, and the food.
    '''
    def __init__(self, size, food='random', hive='random'):
        self.world = [[point]*size]*size
        if hive == 'random':
            hLocation = (random.randint(0,size-1), random.randint(0,size-1))
        else:
            hLocation = hive

        if food == 'random':
            fLocation = (random.randint(0,size-1), random.randint(0,size-1))
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

    def findNeighbours(self, coords):
        x, y = coords
        n = []
        for i in xrange(-1,2):
            for j in xrange(-1,2):
                n.append((x+i,y+j))
        n.sort()

        n = [point for point in n if self.__checkCoords__(point)]

        n.remove(coords)
        return n 

    def __checkCoords__(self, coords):
        x, y = coords
        return (0 <= x < len(self.world)) and (0 <= y < len(self.world))
        


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
    def __init__(self, location, amount=100):
        point.__init__(self, location)
        self.foodLeft = amount

    def removeFood(self):
        self.foodLeft -= 1


