#! /usr/bin/env python

import unittest
import antSearch

class TestPoint(unittest.TestCase):
    
    def setUp(self):
        self.loc = (1,1)
        self.p = antSearch.point(self.loc)

    def test_create(self):
        self.assertEqual(self.p.location, self.loc)
       
    def test_pheremones(self):   
        self.assertEqual(self.p.pheremones, 0)
        self.p.pheremoneAdd()    
        self.assertEqual(self.p.pheremones, 1)
        self.p.pheremoneDecay()
        self.assertEqual(self.p.pheremones, 0)

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.loc = (10,10)
        self.f = antSearch.food(self.loc, 100)

    def test_create(self):
        self.assertEqual(self.f.location, self.loc)

    def test_food(self): 
        self.assertEqual(self.f.foodLeft, 100)
        self.f.removeFood()
        self.assertEqual(self.f.foodLeft, 99)

class TestHive(unittest.TestCase):
    
    def setUp(self):
        self.loc = (10,10)
        self.h = antSearch.hive(self.loc)

    def test_create(self):
        self.assertEqual(self.h.location, self.loc)

    def test_hive(self):
        self.assertEqual(self.h.food, 0)
        self.h.addFood()
        self.assertEqual(self.h.food, 1)


class TestWorld(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_create(self):
        World1 = antSearch.world(100)
        self.assertEqual(len(World1.world), 100)
        self.assertEqual(len(World1.world[0]), 100)

    def test_create_food(self):
        newWorld = antSearch.world(100, food=(1,1))
        self.assertEqual(newWorld.point((12,13)), antSearch.point)
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

    def test_find_neighbours(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        centre1 = (11,34)
        n_sol = [(10,35),(11,35),(12,35),(10,34),(12,34),(10,33),(11,33),(12,33)]
        n_sol.sort()

        World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
        n = World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_top(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        centre1 = (10,0)
        n_sol = [(9,0),(11,0),(9,1),(10,1),(11,1)]
        n_sol.sort()

        World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
        n = World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)
        
    def test_find_neighbours_bottom(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        centre1 = (10,99)
        n_sol = [(9,99),(11,99),(9,98),(10,98),(11,98)]
        n_sol.sort()

        World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
        n = World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_left(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        centre1 = (0,10)
        n_sol = [(0,9),(0,11),(1,9),(1,10),(1,11)]
        n_sol.sort()

        World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
        n = World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_right(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        centre1 = (99,10)
        n_sol = [(99,9),(98,9),(98,10),(98,11),(99,11)]
        n_sol.sort()

        World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
        n = World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_topleft(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        centre1 = (0,0)
        n_sol = [(1,0),(1,1),(0,1)]
        n_sol.sort()

        World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
        n = World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_topright(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        centre1 = (99,0)
        n_sol = [(98,0),(98,1),(99,1)]
        n_sol.sort()

        World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
        n = World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_bottomleft(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        centre1 = (0,99)
        n_sol = [(0,98),(1,98),(1,99)]
        n_sol.sort()

        World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
        n = World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_bottomright(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        centre1 = (99,99)
        n_sol = [(99,98),(98,99),(98,98)]
        n_sol.sort()

        World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
        n = World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

if __name__ == '__main__':
    unittest.main(verbosity=2)

