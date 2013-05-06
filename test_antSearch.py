#! /usr/bin/env python

import unittest
import antSearch

class TestPoint(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_create(self):
        p = antSearch.point((1,1))
        self.assertEqual(p.location, (1,1))
        self.assertEqual(p.pheremones, 0)
        p.pheremoneAdd()    
        self.assertEqual(p.pheremones, 1)
        p.pheremoneDecay()
        self.assertEqual(p.pheremones, 0)

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

if __name__ == '__main__':
    unittest.main(verbosity=2)

