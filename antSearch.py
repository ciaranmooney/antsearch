# Copyright 2013,2014 Ciarán Mooney (general.mooney@googlemail.com)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

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
            print("=============")
            print("Turning ants")   
            for ant in self.ants:
                print("Ant turn", ant)
                ant.turn()
                print("Found food?", ant.haveFood)
            print("=============")
            print("World, turn")
            self.world.turn()
            print("Hive food.", self.world.hive().food)
            print("Food", self.world.food().foodLeft)
            print("Total food", self.world.totalFood)
            print("World finished?", self.world.finished)
            print("=====xxxx========")
        print("====Simulation Finished====")

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
        self.nextPoint = None
        self.moves = []
    
    def preTurn(self):
        ''' Controls an ants pre-turn behaviour. At the moment, in pre-turn an 
            ant just surveys his neighbour points and decides where to go next.
        '''
        
        self.chooseMove()

    def turn(self):
        '''
        Controls what an ant does each turn.
        
        An Ants turn behaviour:
            if ant has no food, check to see on food point
            
            if ant has food then check to see if on hive 
            
            if ant has no food then look for pheremones or food
            move (priority food, pheremones, then empty)
            
            if ant has food but not on food point then deposit pheremone 
            move (priority hive, pheremones, then empty)
        '''
        print("ant turning") 
        print("Current location: "+str(self.location))
        print("Ant Food: "+ str(self.haveFood))
        self.preTurn()

        if self.haveFood == False and isinstance(self.world.point(self.location), food):
            print("Got food!")
            self.world.food().removeFood()
            self.haveFood = True

        if self.haveFood == True and isinstance(self.world.point(self.location), hive):
            self.world.hive().addFood()
            self.haveFood = False

        if self.haveFood == False and isinstance(self.world.point(self.location), hive):
            print("Still in hive")

        if self.haveFood == True and not isinstance(self.world.point(self.location), food):
            print("Ant adding pheremones")
            print(self.location)
            self.world.addPheremone(self.location)

        self.postTurn()
        print("Next point: " + str(self.nextPoint))
        print("ant finish turning")

    def postTurn(self):
        '''
        '''
        self.lastPoint = self.location
        self.location = self.nextPoint
    
    def chooseMove(self):
        ''' Finds neighbours from world. Then checks to see what type of point
            each neighbour is and builds a weighted list.
            
            Chooses a random point from that weighted list.
            
            HaveFood = False
                empty point = *1
                point with x pheremones = *(x+1)
                point with food = *(empty+pheremones)
            
            HaveFood = True
                empty point = *1
                point with x pheremones = *(x+1)
                point with hive = *(empty+pheremones)
        '''
        
        neighbours = self.world.findNeighbours(self.location)
        weights = []
        print(neighbours)
        if self.haveFood == False:
            food_near = False
            while neighbours:
                coord = neighbours.pop()
                p = self.world.point(coord)
                
                if isinstance(p, food):
                    food_near = True
                    food_point = coord

                if isinstance(p, hive):
                    weights.append(coord)

                if p == None:
                    weights.append(coord)

                if isinstance(p, point):
                    pher = p.totalPheremones()
                    if pher > 0:
                        for i in range(pher+1):
                            weights.append(coord)
            if food_near:
                for i in range(len(weights)):
                    weights.append(food_point)

        if self.haveFood == True:
            hive_near = False
            while neighbours:
                coord = neighbours.pop()
                p = self.world.point(coord)

                if isinstance(p, hive):
                    hive_near = True
                    hive_point = coord

                if isinstance(p, food):
                    weights.append(coord)

                if p == None:
                    weights.append(coord)

                if isinstance(p, point):
                    pher = p.totalPheremones()
                    if pher > 0:
                        for i in range(pher+1):
                            weights.append(coord)
            if hive_near:
                for i in range(len(weights)):
                    weights.append(hive_point)

        self.weights = weights
        self.nextPoint = choice(self.weights)
    
    def weighting(self, neighbours, criteria):
        ''' Takes the neighbours list and returns a weighted list based on 
            criteria and the weightFunc
        '''
        pass 
        
    def emptyWeights(self):
        '''
        '''
        
        pass
    
    
    def pheremoneWeights(self):
        '''
        '''
        
        pass


    def hiveWeights(self):
        '''
        '''
        
        pass
    
    
    def foodWeights(self):
        '''
        '''
        
        pass

class world(object):
    ''' World contains the hive, the pheremones, and the food.
    '''
    
    def __init__(self, size, food='random', hive='random', pheremoneDecay=10):
       
        self.world = []
        self.pheremones = []
        self.pheremoneDecayRate = pheremoneDecay
        self.steps = 0
        
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
        ''' Finds coordinates of all adjacent points around the given point. 
            In ideal case you get 8 valid points (3x3 grid with hole in the 
            middle.) Corner and side cases are treated too.
            
            You do not get your original coordinate back. 

            If these contain coordinates contain other obstacles this is for
            the ant to find out.

            Method generates all possible coords for 3x3 square around given 
            coord. Then discards though that lie out of the boundary of the 
            world.
        '''

        x, y = coords
        n = []
        for i in range(-1,2):
            for j in range(-1,2):
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
            print(self.pheremoneDecayRate)
            self.world[x][y] = point(self.pheremoneDecayRate)
            self.world[x][y].pheremoneAdd(self.steps)
            if coords not in self.pheremones:
                self.pheremones.append(coords)
			    
        elif type(self.point(coords)) == point:
            self.world[x][y].pheremoneAdd(self.steps)
            if coords not in self.pheremones:
                self.pheremones.append(coords)

    def removePheremone(self, coords):
        ''' Decreases the pheremone attribute of a point at the coordinates.
        
            Tries to decrease attribute, but possibly no point there. Need
            to catch this error.
            
        '''

        x, y = coords
        p = self.point(coords)
        p.pheremoneDecay(self.steps)   


    def pheremonesLeft(self, point):
        ''' Checks point to see if pheremones > 0
        '''
        
        return self.point(point).totalPheremones() != 0

       
    def pheremoneDecay(self):
        ''' Decreases the pheremone count by one.
			Tidies up self.pheremones to only include points with
			pheremones > 0
        '''
        
        if self.pheremoneDecayRate == 0:
            pass
        elif self.pheremoneDecayRate < 0:
            raise ZeroError
        else:
            for point in self.pheremones:
                self.removePheremone(point)
            
            self.pheremones = filter(self.pheremonesLeft, self.pheremones)
            self.pheremones = list(self.pheremones)


    def turn(self):
        '''
        '''
        
        if self.food().foodLeft == 0 and self.hive().food == self.totalFood:
            self.finished = True
        
        self.pheremoneDecay()
            
        self.steps += 1


class point(object):
    ''' A point in the world. This keeps track of the pheremone trails.
        or food, or hive.
    '''

    # XXX I reckon the point needs a .turn method to control pheremone decay

    def __init__(self, decay):
        ''' Creates an empty list for the pheremones whose size is equal to the
            number of steps required for decaying.
        '''

        self.pheremones  = []
        if decay == 0:
            self.pheremones = 0
        else:
            for i in range(decay):
                self.pheremones.append(0)

    def pheremoneDecay(self, step):
        ''' Sets a value of self.pheremones to zero to indicate decay of the
            pheremone trail.
        '''
        print("Step:", step, "Pheremones", self.pheremones)
        self.pheremones[(step-1) % len(self.pheremones)] = 0
        print("Step:", step, "Pheremones", self.pheremones)

        
    def pheremoneAdd(self, step):
        ''' Increments an entry in self.pheremones which contains the total
            pheremones added for each step.
        '''
        if isinstance(self.pheremones, int):
            self.pheremones = self.pheremones + 1
        else:
            self.pheremones[step % len(self.pheremones)] += 1
        
        
    def totalPheremones(self):
        ''' Inspects self.pheremone and gives an up-to-date total.
        '''
        runningTotal = 0
        
        if isinstance(self.pheremones, int):
            return self.pheremones
        else:
            for i in self.pheremones:
                runningTotal = runningTotal + i
        
            return runningTotal


class hive(object):
    ''' Hive object, keeps track of how much food is collected. So that we can
        figure out if we have reached the end of the simulation.
    '''

    def __init__(self,):
        '''
        '''
        
        self.food = 0


    def addFood(self):
        '''
        '''
        
        self.food += 1


class food(object):
    ''' Food object. Keeps track of how much food is left. 
    '''
    def __init__(self, amount=100):
        '''
        '''
        
        self.foodLeft = amount


    def removeFood(self):
        '''
        '''

        self.foodLeft -= 1


if __name__ == '__main()__':
    pass
