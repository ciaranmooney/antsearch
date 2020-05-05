from food import food
from hive import hive
from point import point

class world(object):
    ''' World contains the hive, the pheremones, and the food.
    '''

    def __init__(self):
        pass

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