#! /usr/bin/env python

import random
from random import choice

class simulation(object):
    '''
    '''

    def __init__(self, ants, world):
        '''
        '''
        self.ants = ants
        self.world = world
        print(self.ants)

    def run(self):
        '''
        '''
        print("Running")
        while not self.world.finished:
            print("Turning ants")   
            for ant in self.ants:
                print("Ant turn", ant)
                ant.turn()
                print("Found food?", ant.haveFood)
            print("World, turn")
            self.world.turn()
            print("Hive food.", self.world.hive().food)
            print("Food", self.world.food().foodLeft)
            print("Total food", self.world.totalFood)
            print("World finished?", self.world.finished)

class ant(object):
    ''' Ants looks for food, when they find it they return home follwing a
        random path. Leaving behind a trail of pheremones.

        Ants always move randomly, but they will weight their choices 
        depending on what is around them.
        
        A point is weighted relative to the number of pheremones it 
        contains. A point with food or a hive is always weighted double 
        the other points.
    
    '''
    def __init__(self, world):
        ''' Initialise ant with world that it is going to search.
        '''    
        self.world = world
        self.haveFood = False
        self.location = self.world.hiveLocation
        self.lastPoint = None
        self.objective = "food"
        self.__moves__ = []
    
    def turn(self):
        '''
        Controls what an ant does each turn.
        
        An Ants turn behaviour:
            check objective
            if food, check to see on food point
            if objective hive then check to see if on hive 
            
            if objective food the look for pheremones or food
            move (priority food, pheremones, then empty)

            if objective hive then look for hive
            
            if not found hive deposit pheremone 
            move (pheremones first priority, then empty)
        '''
        
        if self.objective == 'food' and type(self.world.point(self.location)) == food:
            self.world.food().removeFood()
            self.haveFood = True
            self.objective = 'hive'

        if self.objective == 'hive' and type(self.world.point(self.location)) == hive:
            self.world.hive().addFood()
            self.haveFood = False
            self.objective = 'food'

        self.world.addPheremone(self.location)
        self.move()

    def move(self):
        ''' Finds neighbours from world. Then checks to see what type of point
            each neighbour it and builds a weighted list.
            
            Chooses a random point from that weighted list.
        '''
        self.moves = []
        self.neighbours = self.world.findNeighbours(self.location) 
        
        if self.lastPoint in self.neighbours:
            self.neighbours.remove(self.lastPoint)
        
        if self.objective == 'food':
            for coord in self.neighbours:
                p = self.world.point(coord)
                if hasattr(p, 'pheremones'):
                    for i in range(p.pheremones+1):
                        self.__moves__.append(coord)
                else:
                    self.__moves__.append(coord)

            for coord in self.neighbours:
                multiple = len(self.__moves__)
                if isinstance(self.world.point(coord), food):
                    for i in range(multiple):
                        self.__moves__.append(coord)

        if self.objective == 'hive':
            for coord in self.neighbours:
                p = self.world.point(coord)
                if hasattr(p, 'pheremones'):
                    for i in range(p.pheremones+1):
                        self.__moves__.append(coord)
                else:
                    self.__moves__.append(coord)

            for coord in self.neighbours:
                multiple = len(self.__moves__)
                if isinstance(self.world.point(coord), hive):
                    for i in range(multiple):
                        self.__moves__.append(coord)

        self.__moves__.sort()
        self.lastPoint = self.location
        self.location = choice(self.neighbours)

class world(object):
    ''' World contains the hive, the pheremones, and the food.
    '''
    def __init__(self, size, food='random', hive='random'):
       
        self.world = []
        self.pheremones = []
        self.pheremoneDecayRate = 10
        
        for i in range(size):
            self.world.append([])
            for j in range(size):
                self.world[i].append(None)
     
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
        self.totalFood = self.food().foodLeft

        self.finished = False

    def hive(self):
        ''' Convinience method to quickly get the hive object.
            Returns a hive object.
        '''
        x, y = self.hiveLocation
        return self.world[x][y]

    def food(self):
        ''' Convinience method to quickly get the food object.
            Returns a food object.
        '''
        x, y = self.foodLocation
        return self.world[x][y]

    def create_hive(self):
        ''' Puts a hive object at the location give. Loation is a tuple with
            (x,y) coords.
        '''
        x, y = self.hiveLocation
        self.world[x][y] = hive()

    def create_food(self, amount=100):
        ''' Puts a food object at the location give. Loation is a tuple with
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
        ''' Returns what is at the given coordinate in the world.
            Can either be None, food, hive or point.
        '''
        x, y = coords
        return self.world[x][y]

    def findNeighbours(self, coords):
        ''' Finds coordinates of points around the given point. In ideal case
            you get 8 valid points. Corner and side cases are treated too.
            
            You do not get your original coordinate back. 3x3 grid with hole
            in the middle.

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
        
    def addPheremone(self, coords):
        ''' Leaves a pheremone at the coordinates by incrementing the points
            pheremone attribute.
            
            If there is no point here, one is created and it's pheremone 
            counter incremented by one.
        '''
        x, y = coords
        if self.point(coords) == None:
            self.world[x][y] = point()
            p = self.point(coords)
            p.pheremoneAdd()
            if coords not in self.pheremones:
                self.pheremones.append(coords)
            
        elif type(self.point(coords)) == point:
            p = self.point(coords)
            p.pheremoneAdd()
            if coords not in self.pheremones:
                self.pheremones.append(coords)
        
    def removePheremone(self, coords):
        ''' Decreases the pheremone attribute of a point at the coordinates.
        
            Tries to decrease attribute, but possibly no point there. Need
            to catch this error.
            
        '''
        x, y = coords
        p = self.point(coords)
        try:
            p.pheremoneDecay()
        except:
            print("Error!") 

    def pheremoneDecay(self):
        '''
        '''
        for point in self.pheremones:
            self.removePheremone(point)

    def turn(self):
        '''
        '''
        if self.food().foodLeft == 0 and self.hive().food == self.totalFood:
            self.finished = True
        
        self.pheremoneDecay()
        self.pheremones = filter(lambda x: self.point(x).pheremones != 0, self.pheremones)
        

class point(object):
    ''' A point in the world. This keeps track of the pheremone trails.
        or food, or hive.
    '''
    def __init__(self):
        self.pheremones  = 0
    
    def pheremoneDecay(self):
        if self.pheremones == 0:
            pass
        else:	
            self.pheremones -= 1
    
    def pheremoneAdd(self):
        self.pheremones += 1

class hive(object):
    ''' Hive object, keeps track of how much food is collected. So that we can
        figure out if we have reached the end of the simulation.
    '''
    def __init__(self,):
        self.food = 0

    def addFood(self):
        self.food += 1

class food(object):
    ''' Food object. Keeps track of how much food is left. 
    '''
    def __init__(self, amount=100):
        self.foodLeft = amount

    def removeFood(self):
        self.foodLeft -= 1

if __name__ == '__main()__':
    pass
