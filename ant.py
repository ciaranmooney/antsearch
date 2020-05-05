from random import choice

import food
import hive
import point
from food import food
from hive import hive
from point import point


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
        self.preTurn()

        if self.haveFood == False and isinstance(point.point(self.location), food):
            food.food().removeFood()
            self.haveFood = True

        if self.haveFood == True and isinstance(point.point(self.location), hive):
            hive.hive().addFood()
            self.haveFood = False

        if self.haveFood == False and isinstance(point.point(self.location), hive):
            pass # Still in hive?

        if self.haveFood == True and not isinstance(point.point(self.location), food):
            self.world.addPheremone(self.location)

        self.postTurn()

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
        if self.haveFood == False:
            food_near = False
            while neighbours:
                coord = neighbours.pop()
                p = point.point(coord)

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
                p = point.point(coord)

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