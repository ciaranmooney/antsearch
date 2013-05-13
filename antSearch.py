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
        ''' Initialise ant with world that it is going to search.
        '''    
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
        ''' When travelling across points with food the ant must leave behind
            a pheremone trail. This increments the points pheremone counter by
            one.
        '''
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
        self.world = [[None]*size]*size
        
        for i in range(size):
            self.world.append([])
            for j in range(size):
                self.world[i].append(point())
     
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

        self.create_hive()
        self.create_food()
        self.totalFood = self.point(self.foodLocation).foodLeft

    def hive(self):
        ''' Convinience method to quickly get the hive object.
        '''
        x, y = self.hiveLocation
        return self.world[x][y]

    def food(self):
        ''' Convinience method to quickly get the food object.
        '''
        x, y = self.foodLocation
        return self.world[x][y]

    def create_hive(self, hiveLocation):
        ''' Puts a hive object at the location give. Loation is a tuple with
            (x,y) coords.
        '''
        x, y = self.hiveLocation
        self.world[x][y] = hive()

    def create_food(self, amount=100):
        ''' Puts a hive object at the location give. Loation is a tuple with
            (x,y) coords.
        '''
        x, y = self.foodLocation
        self.world[x][y] = food(amount)

    def show_world(self):
        ''' Shows world in a nice text format for printing to terminal with 
            pheremones, food and hive. Intended to show ants too but this may 
            not actually happen here and be added on later. Maybe replaced 
            with __str__()
        '''
        return self.world

    def point(self, coords):
        ''' Returns what is at a point in the world.
        '''
        x, y = coords
        return self.world[x][y]

    def findNeighbours(self, coords):
        ''' Finds coordinates of points around the given point. In ideal case
            you get 8 valid points. Corner and side cases are treated too.
            
            You do not get your original coordinate back.

            If these contain coordinates contain other obstacles this is for
            the ant to find out.

            Method generates all possible coords for 3x3 square around given 
            coord. Then discards though that lie out of the boundary of the 
            world.
        '''
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
        ''' Check if point lies within the boundary of the world.
        '''
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


