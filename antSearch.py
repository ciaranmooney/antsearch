#! /usr/bin/env python

import random
from random import choice

class ant(object):
    ''' Ants looks for food, when they find it they return home follwing a
        random path. Leaving behind a trail of pheremones.

        Ants look randomly, unless they see a pheremone trail. If they see
        multiple trails they follow the strongest.
    
    '''
    def __init__(self, world):
        self.world = world
        self.have_food = False
        self.location = self.world.hiveLocation
        self.lastPoint = None
        self.objective = "food"
        self.__moves__ = []
    
    def turn(self):
        '''
        An Ants turn behaviour:
            check objective
            if food, check to see on food point
            if objective food the look for pheremones or food
            move (priority food, pheremones, then empty)

            if objective hive then check to see if on hive 
            if objective hive then look for hive
            if not found hive deposit pheremone 
            look for pheremones
            move (pheremones first priority, then empty)
        '''
        self.move()

    def move(self):
        ''' Choose and move to new location
        '''
        self.neighbours = self.world.findNeighbours(self.location) 
        
        if self.lastPoint in self.neighbours:
            self.neighbours.remove(self.lastPoint)
        
        if self.objective == 'food':
            for coord in self.neighbours:
                p = self.world.point(coord)
                if hasattr(p, 'pheremones'):
                    print "found pheremone", p.pheremones, coord 
                    for i in range(p.pheremones):
                        self.__moves__.append(coord)
                else:
                    self.__moves__.append(coord)

            for coord in self.neighbours:
                multiple = len(self.__moves__)
                if isinstance(self.world.point(coord), food):
                    for i in range(multiple):
                        self.__moves__.append(coord)
                        self.__moves__.append(coord)

        if self.objective == 'hive':
            for coord in self.neighbours:
                if type(self.world.point(coord)) == hive:
                    self.__moves__.append(coord)
                    self.__moves__.append(coord)
                    self.__moves__.append(coord)

                elif type(self.world.point(coord)) == pheremone:
                    self.__moves__.append(coord)
                    self.__moves__.append(coord)
                else:
                    self.__moves__.append(coord)

        print "moves", self.__moves__
        self.lastPoint = self.location
        self.location = choice(self.neighbours)
       
    def leavePheremone(self):
        pass
    
    def checkSurroundings(self):
        pass

    def foundFood(self):
        pass

    def returnHome(self):
        pass

class world(object):
    ''' World contains the hive, the pheremones, and the food.
    '''
    def __init__(self, size, food='random', hive='random'):
        self.world = [None]*size
        for i in range(size):
             self.world[i] = [point()] * size
     
        i#self.world = [[point]*size]*size
        
        if hive == 'random':
            hLocation = (random.randint(0,size-1), random.randint(0,size-1))
        else:
            hLocation = hive

        if food == 'random':
            fLocation = (random.randint(0,size-1), random.randint(0,size-1))
        else:
            fLocation = food

        self.hiveLocation = hLocation
        self.foodLocation = fLocation

        self.create_hive(self.hiveLocation)
        self.create_food()
        self.totalFood = self.point(self.foodLocation).foodLeft

    def hive(self):
        x, y = self.hiveLocation
        return self.world[x][y]

    def food(self):
        x, y = self.foodLocation
        return self.world[x][y]

    def create_hive(self, hiveLocation):
        self.hiveLocation = hiveLocation
        x, y = hiveLocation
        self.world[x][y] = hive()

    def create_food(self, amount=100):
        x, y = self.foodLocation
        self.world[x][y] = food(amount)

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
    def __init__(self):
#        self.location = location
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
    def __init__(self,):
        point.__init__(self)
        self.food = 0

    def addFood(self):
        self.food += 1

class food(point):
    ''' Food object. Keeps track of how much food is left. 
    '''
    def __init__(self, amount=100):
        point.__init__(self,)
        self.foodLeft = amount

    def removeFood(self):
        self.foodLeft -= 1


