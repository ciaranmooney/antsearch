#! /usr/bin/env python

import unittest
import antSearch

class TestWorld(unittest.TestCase):

    def setUp(self):
        pass

    def test_create(self):
        newWorld = antSearch.world(100)
        assert(len(newWorld) == 100)
        assert(len(newWorld[0] == 100)

class TestAnt(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_initialise(self):
        new_ant = antSearch.ant() 

if __name__ == '__main__':
    unittest.main()
