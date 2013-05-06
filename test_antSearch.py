#! /usr/bin/env python

import unittest
import antSearch

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
        print(newWorld.point((1,1)))
        food = newWorld.point((1,1))
        print(food.foodLeft)
        
        self.assertEqual(newWorld.point((1,1)).foodLeft, 100)

class TestPoint(unittest.TestCase):
    pass

#class TestAnt(unittest.TestCase):
#    
#    def setUp(self):
#        pass
#    
#    def test_initialise(self):
#        new_ant = antSearch.ant() 

if __name__ == '__main__':
    unittest.main()

