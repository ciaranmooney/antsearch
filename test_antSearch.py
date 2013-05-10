#! /usr/bin/env python

import unittest
import antSearch

class TestPoint(unittest.TestCase):
    
    def setUp(self):
        self.p = antSearch.point()

    def test_create(self):
        pass
        #self.assertEqual(self.p.location, self.loc)
       
    def test_pheremones(self):   
        self.p.pheremoneAdd()    
        self.assertEqual(self.p.pheremones, 1)
        self.p.pheremoneDecay()
        self.assertEqual(self.p.pheremones, 0)

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.loc = (10,10)
        self.f = antSearch.food(100)

    def test_food(self): 
        self.assertEqual(self.f.foodLeft, 100)
        self.f.removeFood()
        self.assertEqual(self.f.foodLeft, 99)

class TestHive(unittest.TestCase):
    
    def setUp(self):
        self.h = antSearch.hive()

    def test_hive(self):
        self.assertEqual(self.h.food, 0)
        self.h.addFood()
        self.assertEqual(self.h.food, 1)


class TestWorld(unittest.TestCase):
    
    def setUp(self):
        self.test_find_neighbours_setUp()
    
    def test_find_neighbours_setUp(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        self.World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
    
    def test_create(self):
        World1 = antSearch.world(100)
        self.assertEqual(len(World1.world), 100)
        self.assertEqual(len(World1.world[0]), 100)

    def test_create_point(self):
        coord = (30,20)
        p = self.World3.point(coord)
        self.assertEqual(p.pheremones, 0)
        self.assertEqual(type(p), antSearch.point)

    def test_create_food(self):
        newWorld = antSearch.world(100, food=(1,1))
        self.assertEqual(type(newWorld.point((12,13))), antSearch.point)
        self.assertEqual(type(newWorld.point((1,1))), antSearch.food)
        food = newWorld.point((1,1))
        self.assertEqual(newWorld.point((1,1)).foodLeft, 100)
        self.assertEqual(newWorld.totalFood, 100)

    def test_create_hive(self):
        hiveLocation = (10,10)
        World2 = antSearch.world(100, hive=hiveLocation)
        self.assertEqual(type(World2.point(hiveLocation)), antSearch.hive)
        hive = World2.point((10,10))
        self.assertEqual(hive.food, 0)
        hive.addFood()
        self.assertEqual(hive.food, 1)

    def test_hive(self):
        hiveLocation = (10,10)
        World2 = antSearch.world(100, hive=hiveLocation)
        
        self.assertEqual(type(World2.hive()), antSearch.hive)
        self.assertEqual(World2.hiveLocation, hiveLocation)

    def test_food(self):
        foodLocation = (52,40)
        World2 = antSearch.world(100, food=foodLocation)
        
        self.assertEqual(type(World2.food()), antSearch.food)
        self.assertEqual(World2.foodLocation, foodLocation)

    def test_find_neighbours(self):
        centre1 = (11,34)
        n_sol = [(10,35),(11,35),(12,35),(10,34),(12,34),(10,33),(11,33),(12,33)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_top(self):
        centre1 = (10,0)
        n_sol = [(9,0),(11,0),(9,1),(10,1),(11,1)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)
        
    def test_find_neighbours_bottom(self):
        centre1 = (10,99)
        n_sol = [(9,99),(11,99),(9,98),(10,98),(11,98)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_left(self):
        centre1 = (0,10)
        n_sol = [(0,9),(0,11),(1,9),(1,10),(1,11)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_right(self):
        centre1 = (99,10)
        n_sol = [(99,9),(98,9),(98,10),(98,11),(99,11)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_topleft(self):
        centre1 = (0,0)
        n_sol = [(1,0),(1,1),(0,1)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_topright(self):
        centre1 = (99,0)
        n_sol = [(98,0),(98,1),(99,1)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_bottomleft(self):
        centre1 = (0,99)
        n_sol = [(0,98),(1,98),(1,99)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_bottomright(self):
        centre1 = (99,99)
        n_sol = [(99,98),(98,99),(98,98)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)


class TestAnt(unittest.TestCase):
    
    def setUp(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        self.world = antSearch.world(100, hive=hiveLocation, food=foodLocation)

    def test_init(self):
        ant = antSearch.ant(self.world)

        self.assertEqual(ant.world, self.world)
        self.assertEqual(ant.have_food, False)
        self.assertEqual(ant.location, self.world.hiveLocation)
        self.assertEqual(ant.objective, 'food')

    def test_turn(self):
        ant = antSearch.ant(self.world) 
        
        self.assertEqual(ant.location, self.world.hiveLocation)
        possible_moves = self.world.findNeighbours(ant.location) 

        ant.turn()
        self.assertEqual(ant.location in possible_moves, True)
   
    def test_turn_pheremone(self):
        ant = antSearch.ant(self.world) 
        ant.location = (50,50)
        
        self.world.point((49,49)).pheremones = 1
        print "Pheremone test", self.world.point((49,49)).pheremones

        possible_moves = self.world.findNeighbours(ant.location) 
        possible_moves.append((49,49))
        possible_moves.sort()
        ant.turn()
        print "test", possible_moves
        self.assertEqual(ant.__moves__, possible_moves)

    def test_move(self):
        ant = antSearch.ant(self.world)

        self.assertEqual(ant.location, self.world.hiveLocation)
        
        possible_moves = self.world.findNeighbours(ant.location) 
       
        ant.move()
        
        self.assertEqual(ant.location in possible_moves, True)
        self.assertEqual(ant.lastPoint, self.world.hiveLocation)

        test_point = ant.location
        possible_moves = self.world.findNeighbours(ant.location) 
       
        ant.move()
        
        self.assertEqual(ant.location in possible_moves, True)
        self.assertEqual(ant.lastPoint, test_point)

    def test_move_pheremone(self):
        pass

    def test_move_food(self):
        pass

    def test_move_hive(self):
        pass

    def test_check_surroundings(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)

