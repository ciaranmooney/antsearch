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

import unittest
import antSearch

class Simulation(unittest.TestCase):
    '''
    '''

    def setUp(self):
        '''
        '''
        pass

    def test_simulation_1x2(self):
        ''' 1D array with 2 spaces. Hive in one, food in other. An ant should
            move food from food point to hive point.
            
            No phermeones should be deposited.
        '''
        
        fLoc = (0,1)
        hLoc = (0,0)
        decayRate = 0
        self.world = antSearch.world(3, fLoc, hLoc, decayRate)
        ## XXX ###
        # .world() init syntax is for number to be size of array
        # ie 1 = 1x1, 2 = 2x2. need to change to be (3), (3,3) or (1,2)
        self.ants = []
        self.ants.append(antSearch.ant(self.world))
       
        food = self.world.food()
        food.foodLeft = 1
        self.world.totalFood = 1

        self.assertEqual(self.world.food(), food)
        self.assertEqual(type(self.world.hive()), antSearch.hive)

        self.assertEqual(self.world.hive().food, 0)
        self.assertEqual(self.world.food().foodLeft, 1)
        
        sim = antSearch.simulation(self.ants, self.world)

        #sim.run()

        self.assertEqual(self.world.hive().food, 1)
        self.assertEqual(self.world.food().foodLeft, 0)

        self.assertTrue(False)
        
    def test_simulation_1x3(self):
        ''' 1D array with 3 spaces. Have in far left, food far right. An ant
            should move the food from the food to the hive depositing one
            pheremone in the middle.
        '''
        
        self.assertTrue(False)

    def test_simulation_3x3(self):
        ''' Create a 3x3 grid with food and hive in opposite corners. 
            Have one ant.

            Run Simulation.

            Check to see that food in hive is 1
            Check to see food point is empty.
            Check world has pheremones.

        '''
        fLoc = (2,2)
        hLoc = (0,0)
        decayRate = 0
        self.world = antSearch.world(3, fLoc, hLoc, decayRate)
        self.ants = []
        self.ants.append(antSearch.ant(self.world))
       
        self.food = self.world.food()
        self.food.foodLeft = 1
        self.world.totalFood = 1

        self.assertEqual(self.world.food(), self.food)
        self.assertEqual(type(self.world.hive()), antSearch.hive)

        self.assertEqual(self.world.hive().food, 0)
        self.assertEqual(self.world.food().foodLeft, 1)
        
        sim = antSearch.simulation(self.ants, self.world)

        sim.run()

        self.assertEqual(self.world.hive().food, 1)
        self.assertEqual(self.world.food().foodLeft, 0)

        self.assertTrue(len(self.world.pheremones) > 0)
        

class TestPoint(unittest.TestCase):
    ''' Tests for the Point Class
    ''' 

    def setUp(self):
        ''' Creates new point for each test.
        '''
        
        self.decay = 10
        self.p = antSearch.point(self.decay)
    
    
    def test_new_pheremone_list_empty(self):
        ''' Tests that the pheremone list created in the point class is the
            expected length and contains all zeros.
        '''
        
        self.assertEqual(len(self.p.pheremones), self.decay)
        
        for i in self.p.pheremones:
            self.assertEqual(i, 0)
        
        
    def test_new_pheremone_zero(self):   
        ''' Tests that when a point is created that it has no 
            pheremones.
        '''
        
        self.assertEqual(self.p.totalPheremones(), 0)
        self.assertNotEqual(self.p.totalPheremones(), -1)
        self.assertNotEqual(self.p.totalPheremones(), 1)
        
        
    def test_addPheremones(self):
        ''' Tests new point has no pheremones. Then checks that the structure of
            self.p.phereemones is correct after point.pheremoneAdd(step) is
             called.
            
            Checks that a new phermeone with a new step value is added if a
            different step value is given.
            
            Nb. Fragile test. Depends on self.decay remaining equal to 10
        '''
                
        self.assertEqual(self.p.totalPheremones(), 0)        
        self.p.pheremoneAdd(0)  # step one        
        self.assertEqual(self.p.pheremones, [1,0,0,0,0,0,0,0,0,0])
        self.p.pheremoneAdd(1) # step two
        self.assertEqual(self.p.pheremones, [1,1,0,0,0,0,0,0,0,0])
        
        
    def test_totalPheremones(self):
        ''' Checks that the totalPheremones method of point is working properly.
        
            Checks that a two pheremoneAdds on the same step increase total, and
            another pheremoneAdd on another step increases total.
        '''
        
        self.assertEqual(self.p.totalPheremones(), 0)
        
        self.p.pheremoneAdd(0)  # pheremone at step one
        
        self.assertEqual(self.p.totalPheremones(), 1)
        self.assertNotEqual(self.p.totalPheremones(), 2)
        self.assertNotEqual(self.p.totalPheremones(), 0)
        self.assertNotEqual(self.p.totalPheremones(), -1)

        self.p.pheremoneAdd(0) # Another pheremone at step one
        
        self.assertEqual(self.p.totalPheremones(), 2)
        self.assertNotEqual(self.p.totalPheremones(), 3)
        self.assertNotEqual(self.p.totalPheremones(), 1)
        self.assertNotEqual(self.p.totalPheremones(), -1)
        
        self.p.pheremoneAdd(1) # pheremone at step two
        
        self.assertEqual(self.p.totalPheremones(), 3)
        self.assertNotEqual(self.p.totalPheremones(), 4)
        self.assertNotEqual(self.p.totalPheremones(), 2)
        self.assertNotEqual(self.p.totalPheremones(), -1)
        self.assertNotEqual(self.p.totalPheremones(), 0)
        
        
    def test_multiple_addPheremones(self):
        ''' Tests for when multiple ants add pheremones in the the same turn.
            This will mean the corresponding tuple in point.pheremones will have
            mutliple pheremones for a step.
            
            Nb. Fragile test, depends on self.decay being equal to 10.
        '''
        
        self.assertEqual(self.p.totalPheremones(), 0)
        self.p.pheremoneAdd(0)  # first pheremone added in step 1
        self.p.pheremoneAdd(0)  # second pheremone added in step 1
        
        self.assertEqual(self.p.pheremones, [2,0,0,0,0,0,0,0,0,0])
        
        
    def test_pheremoneDecay(self):
        ''' Tests when a point is created it has no pheremones. 
            Then adds pheremones and checks it decays to zero but not below.            
        '''
        
        self.assertEqual(self.p.totalPheremones(), 0)
        self.p.pheremoneAdd(1)  # step 1
        self.assertEqual(self.p.totalPheremones(), 1)
        self.p.pheremoneDecay(1)
        self.assertEqual(self.p.totalPheremones(), 0)
        self.p.pheremoneDecay(1)
        self.assertEqual(self.p.totalPheremones(), 0)
        self.assertNotEqual(self.p.totalPheremones(), -1)
        

    def test_pheremoneDecay_oldest_first(self):
        ''' Tests that different pheremones on the same point will decay at 
            different times depending on which step they were added.
            
            Should decay from oldest to newest.
            
            Nb. Fragile test dependant on self.decay being equal to 10.
        '''

        self.assertEqual(self.p.totalPheremones(), 0)
        self.p.pheremoneAdd(0)  # step 1
        self.assertEqual(self.p.pheremones, [1,0,0,0,0,0,0,0,0,0])
        self.p.pheremoneAdd(0)  # step 1
        self.assertEqual(self.p.pheremones, [2,0,0,0,0,0,0,0,0,0])
        self.p.pheremoneAdd(1)  # step 2
        self.assertEqual(self.p.pheremones, [2,1,0,0,0,0,0,0,0,0])
        self.p.pheremoneDecay(10) # step 10
        self.assertEqual(self.p.pheremones, [2,1,0,0,0,0,0,0,0,0])
        self.p.pheremoneDecay(11) # step 11
        self.assertEqual(self.p.pheremones, [0,1,0,0,0,0,0,0,0,0])
        self.p.pheremoneDecay(12) # step 12
        self.assertEqual(self.p.pheremones, [0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(self.p.totalPheremones(), 0)
        

class TestFood(unittest.TestCase):
    ''' Tests for food class.
    '''

    def setUp(self):
        '''
        '''
        self.f = antSearch.food(100)

    def test_food(self): 
        '''
        '''
        self.assertEqual(self.f.foodLeft, 100)
        self.f.removeFood()
        self.assertEqual(self.f.foodLeft, 99)

class TestHive(unittest.TestCase):
    ''' Tests for food hive class.
    '''

    def setUp(self):
        '''
        '''
        self.h = antSearch.hive()

    def test_hive(self):
        '''
        '''
        self.assertEqual(self.h.food, 0)
        self.h.addFood()
        self.assertEqual(self.h.food, 1)

class TestWorld(unittest.TestCase):
    ''' Tests for World class.
    '''

    def setUp(self):
        ''' 
        '''
        self.find_neighbours_setUp()
    
    def find_neighbours_setUp(self):
        ''' Creates a new attribute for the test class that is "plain".
            Creates a "default" hive and food location.
        '''
        hiveLocation = (10,10)
        foodLocation = (99,2)
        self.World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
    
    def test_create(self):
        ''' Creates world and checks that the overall size is correct 
            and that the size of the zeroth row is correct.
        '''
        World1 = antSearch.world(100)
        self.assertEqual(len(World1.world), 100)
        self.assertEqual(len(World1.world[0]), 100)

    def test_world_empty(self):
        ''' Tests that the world that has been created is empty at 
            (3,3).
        '''
        p = self.World3.point((3,3))
        self.assertEqual(p, None)

    def test_create_food(self):
        ''' Tests creating a new world, adding food and checking that
            the totals all match up.
        '''
        newWorld = antSearch.world(100, food=(1,1))
        
        self.assertEqual(newWorld.point((12,13)), None)
        self.assertEqual(type(newWorld.point((1,1))), antSearch.food)    
        self.assertEqual(newWorld.point((1,1)).foodLeft, 100)
        self.assertEqual(newWorld.totalFood, 100)

    def test_change_food(self):
        ''' 
        '''
        newWorld = antSearch.world(100, food=(1,1))
        food = newWorld.food()
        self.assertEqual(food.foodLeft, 100)
        self.assertEqual(newWorld.food().foodLeft, 100)

        food.foodLeft = 1

        self.assertEqual(food.foodLeft, 1)
        self.assertEqual(newWorld.food().foodLeft, 1)

    def test_create_hive(self):
        '''
        '''
        hiveLocation = (10,10)
        World2 = antSearch.world(100, hive=hiveLocation)
        self.assertEqual(type(World2.point(hiveLocation)), antSearch.hive)
        hive = World2.point((10,10))
        self.assertEqual(hive.food, 0)
        hive.addFood()
        self.assertEqual(hive.food, 1)

    def test_hive(self):
        '''
        '''
        hiveLocation = (10,10)
        World2 = antSearch.world(100, hive=hiveLocation)
        
        self.assertEqual(type(World2.hive()), antSearch.hive)
        self.assertEqual(World2.hiveLocation, hiveLocation)

    def test_food(self):
        '''
        '''
        foodLocation = (52,40)
        World2 = antSearch.world(100, food=foodLocation)
        
        self.assertEqual(type(World2.food()), antSearch.food)
        self.assertEqual(World2.foodLocation, foodLocation)
        
    def test_food_finished(self):
        '''
        '''
        foodLocation = (52,40)
        World2 = antSearch.world(100, food=foodLocation)
        
        self.assertEqual(World2.food().foodLeft, 100)
        self.assertEqual(World2.hive().food, 0)
        
        World2.food().foodLeft = 0
        World2.hive().food = 100 
        
        self.assertEqual(World2.hive().food, 100)
        self.assertEqual(World2.food().foodLeft, 0)

    def test_find_neighbours(self):
        ''' Checks that world.findNeighbours returns a list of points around a
            centre point.
            
            The list should be equivalent to a 3x3 grid with a hole in the
            middle.
        '''
        centre1 = (11,34)
        n_sol = [(10,35),(11,35),(12,35),
                 (10,34),        (12,34),
                 (10,33),(11,33),(12,33)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_top(self):
        '''
        '''
        centre1 = (10,0)
        n_sol = [(9,0),(11,0),(9,1),(10,1),(11,1)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)
        
    def test_find_neighbours_bottom(self):
        '''
        '''
        centre1 = (10,99)
        n_sol = [(9,99),(11,99),(9,98),(10,98),(11,98)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_left(self):
        '''
        '''
        centre1 = (0,10)
        n_sol = [(0,9),(0,11),(1,9),(1,10),(1,11)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_right(self):
        '''
        '''
        centre1 = (99,10)
        n_sol = [(99,9),(98,9),(98,10),(98,11),(99,11)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_topleft(self):
        '''
        '''
        centre1 = (0,0)
        n_sol = [(1,0),(1,1),(0,1)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_topright(self):
        '''
        '''
        centre1 = (99,0)
        n_sol = [(98,0),(98,1),(99,1)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_bottomleft(self):
        '''
        '''
        centre1 = (0,99)
        n_sol = [(0,98),(1,98),(1,99)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_find_neighbours_bottomright(self):
        '''
        '''
        centre1 = (99,99)
        n_sol = [(99,98),(98,99),(98,98)]
        n_sol.sort()

        n = self.World3.findNeighbours(centre1)
        self.assertEqual(n, n_sol)

    def test_addPheremone_empty_point(self):
        '''
        '''
        point = (49,49)
        self.assertEqual(self.World3.point(point), None)
        self.World3.addPheremone(point)
        self.assertEqual(self.World3.point(point).totalPheremones(), 1)
        self.World3.addPheremone(point)
        self.assertEqual(self.World3.point(point).totalPheremones(), 2)
        
        self.assertEqual(self.World3.pheremones, [point])

    def test_addPheremone_empty_point_zero_deay(self):
        ''' Tests that adding pheremones to a point with decay rate set to
            zero work.
        '''
        point = (49,49)
        self.World3.pheremoneDecayRate=0
        self.assertEqual(self.World3.point(point), None)
        self.World3.addPheremone(point)
        self.assertEqual(self.World3.point(point).totalPheremones(), 1)
        self.World3.addPheremone(point)
        self.assertEqual(self.World3.point(point).totalPheremones(), 2)
        
        self.assertEqual(self.World3.pheremones, [point])
        
        self.assertTrue(False)
    
    def test_addPheremone_hive_point(self):
        '''
        '''
        h = self.World3.hive()
        f = self.World3.food()
        
        hCheck = hasattr(h, 'pheremones')
        fCheck = hasattr(f, 'pheremones')
        self.assertFalse(fCheck)
        self.assertFalse(hCheck)

        self.World3.addPheremone(self.World3.hiveLocation)
        self.World3.addPheremone(self.World3.foodLocation)

        hCheck = hasattr(h, 'pheremones')
        fCheck = hasattr(f, 'pheremones')
        self.assertFalse(fCheck)
        self.assertFalse(hCheck)
    
    def test_removePheremone(self):
        '''
        '''
        point = (50,50)
        self.assertEqual(self.World3.point(point), None)
        self.World3.addPheremone(point)
        self.assertEqual(self.World3.point(point).totalPheremones(), 1)
        self.World3.removePheremone(point)
        self.assertEqual(self.World3.point(point).totalPheremones(), 0)

    def test_turn_world_finished(self):
        '''
        '''
        self.assertFalse(self.World3.finished) 
        self.World3.turn()
        self.assertFalse(self.World3.finished) 

        self.World3.hive().food = self.World3.food().foodLeft
        self.World3.food().foodLeft = 0

        self.assertFalse(self.World3.finished) 
        self.World3.turn()
        self.assertTrue(self.World3.finished)

    def test_print_world(self):
        ''' World will have spaces where there are Nones,
        '''
        self.assertTrue(False)

    def test_world_pheremoneDecay(self):
        ''' Tests that pheremoneDecay method reduces a number of 
            different points pheremone count by one. Also checks that
            pheremonedecay method does not go below zero.
            
        '''
        coords = [(2,10),(10,2),(5,30),(55,21),(59,60),(82,15)]
        
        for i in coords:
            self.World3.addPheremone(i)

        for i in coords:
            self.assertEqual(self.World3.point(i).totalPheremones(), 1)

        self.World3.pheremoneDecay()

        for i in coords:
            self.assertEqual(self.World3.point(i).totalPheremones(), 0)
            
        self.World3.pheremoneDecay()

        for i in coords:
            self.assertEqual(self.World3.point(i).totalPheremones(), 0)
        
    def test_pheremoneDecay_rate(self):
        ''' Checks that the pheremone decay of a world happens at the 
            rate specific (ie per number of turns)
        '''
        
        # Each pheremone has a slightly different decay time as it will
        # depend on when it is depositied.

        p = (1,1)
        self.World3.pheremoneDecayRate = 3

        self.assertEqual(self.World3.point(p), None)
        self.World3.turn() 
        self.assertEqual(self.World3.point(p), None)
        self.World3.addPheremone(p)
        self.assertEqual(self.World3.point(p).totalPheremones(), 1)
        
        self.World3.turn() 
        self.assertEqual(self.World3.point(p).totalPheremones(), 1)
       
        self.World3.turn() 
        self.assertEqual(self.World3.point(p).totalPheremones(), 0)
        
    def test_pheremoneDecay_rate_different(self):
        ''' Creates pheremone at different steps of the simulation and
            checks that they decay away at the expected time.
            
        
            ie, for decay rate of 2 steps, with two pheremones added one
                after the other:
                
               step 1, pheremone 0
               step 2, pheremone 1
               step 3, pheremone 2
               step 4, pheremone 1
               step 5, pheremone 0
        '''
        
        self.assertTrue(False)
            
    def test_pheremonDecay_zero(self):
        ''' Checks that if pheremone decay rate is set to zero that 
            the world doesn't fall over.            
        '''
        
        self.assertTrue(False)

    def test_pheremone_list(self):
        ''' Test that when pheremone reaches 0 that it is removed from
            the pheremone list.
        '''
        
        self.World3.addPheremone((1,1))

        self.assertEqual(self.World3.point((1,1)).totalPheremones(), 1)

        self.World3.pheremoneDecay()
        
        self.assertEqual(self.World3.point((1,1)).totalPheremones(), 0)
        self.assertTrue((1,1) not in self.World3.pheremones)
        
        
    def test_steps_create(self):
        ''' Checks that the steps attribute is created.
        '''
        
        self.assertFalse(self.World3.steps, -1)
        self.assertFalse(self.World3.steps, 1)
        self.assertEqual(self.World3.steps, 0)
        
        
    def test_steps_increment(self):
        ''' Check that after a set number of steps that the steps
            attribute of the world increments.
        '''
        
        self.assertEqual(self.World3.steps,0)
        self.World3.turn()
        self.assertEqual(self.World3.steps,1)
        self.assertNotEqual(self.World3.steps,-1)


class TestAnt(unittest.TestCase):
    ''' A set of tests to make sure that the Ant class is behaving as it should.
    '''


    def setUp(self):
        ''' Creates a world for use in tests with a hive and food in the same 
            location for all the tests.
            
            Creates an ant within this world for the tests.
        '''
        
        hiveLocation = (10,10)
        foodLocation = (99,2)
        self.world = antSearch.world(100, hive=hiveLocation, food=foodLocation)
        self.ant = antSearch.ant(self.world) 


    def test_init(self):
        ''' Tests that the ant is created correctly.
            These tests check that the ant:
            
            * is in the correct world.
            * has no food when created
            * by default is located at the same point as the hive
        '''
        
        self.assertEqual(self.ant.world, self.world)
        self.assertEqual(self.ant.haveFood, False)
        self.assertEqual(self.ant.location, self.world.hiveLocation)


    def test_pre_turn_next(self):
        ''' Searches world for negibourhing spots checks that the spot the ant
            has chosen is in that neighbouring set.
            
            Checks that ant has chosen a valid coordinate.
        '''
        
        self.assertEqual(self.ant.location, self.world.hiveLocation)
        possible_moves = self.world.findNeighbours(self.ant.location)

        self.ant.preTurn()
        
        self.assertEqual(self.ant.nextPoint in possible_moves, True)

    def test_pre_turn_pheremones(self):
        ''' Tests, in an ants pre-turn step, that it has correctly prioritised 
            choosing a point with pheremones over empty adjacent points.
        '''
        
        self.ant.location = (50,50)
        self.world.addPheremone((49,50))
        expected_weights = [(49,50),(49,50), (49,49),(50,49),(51,49),(51,50),
                   (49,51),(50,51),(51,51)]
        expected_weights.sort()
        self.ant.turn()
        ant_weights = self.ant.weights
        ant_weights.sort()
        self.assertEqual(ant_weights, expected_weights)
    
    
    def test_pre_turn_priorties_hive_food(self):
        ''' Tests, in an ants pre-turn step, that when an ant has food, it 
            correctly prioritises choosing a hive over empty adjacent points
        '''
        
        self.ant.location = (9,9)
        self.ant.haveFood = True 
        expected_weights = [(8,8),(9,8),(10,8),(8,9),(10,9),(8,10),
                   (9,10),(10,10),(10,10),(10,10),(10,10),(10,10),
                   (10,10),(10,10)]
        expected_weights.sort()
        self.ant.turn()
        ant_weights = self.ant.weights
        ant_weights.sort()
        self.assertEqual(ant_weights, expected_weights)
    

    def test_pre_turn_priorties_hive_no_food(self):
        ''' Tests, in an ants pre-turn step, that when an ant does not have food
            it does not prioritise a hive.
        '''
        
        self.ant.location = (9,9)
        expected_weights = [(8,8),(9,8),(10,8),(8,9),(10,9),(8,10),
                   (9,10),(10,10)]
        expected_weights.sort()
        self.ant.turn()
        ant_weights = self.ant.weights
        ant_weights.sort()
        self.assertEqual(ant_weights, expected_weights)
       

    def test_pre_turn_priorties_food_no_food(self):
        ''' Tests, in an ants pre-turn step, that when an ant has no food that 
            it has correctly prioritises choosing a food point over empty 
            adjacent points.
        '''
        
        self.ant.location = (99,1)
        expected_weights = [(98,0),(99,0),(98,1),(98,2),(99,2),(99,2),(99,2),
                            (99,2)]
        expected_weights.sort()
        self.ant.turn()
        ant_weights = self.ant.weights
        ant_weights.sort()
        self.assertEqual(ant_weights, expected_weights)
        
    
    def test_pre_turn_priorties_food_food(self):
        ''' Tests, in an ants pre-turn step, that when an ant has food that it 
            has not prioritised choosing a food point over empty adjacent 
            points.
        '''
        
        self.ant.location = (99,1)
        self.ant.haveFood = True
        expected_weights = [(98,0),(99,0),(98,1),(98,2),(99,2)]
        expected_weights.sort()
        self.ant.turn()
        ant_weights = self.ant.weights
        ant_weights.sort()
        self.assertEqual(ant_weights, expected_weights)

    def test_pre_turn_priorities_multiple_food(self):
        ''' Tests that when an ant has food and is adjacent to a hive,
            pheremones, and empty points that it priorites the next step in the
            following order. 
            
            priority hive, pheremones, then empty
        '''
        
        self.ant.location = (10,9)
        self.ant.haveFood = True
        self.world.addPheremone((9,8))
        self.world.addPheremone((9,8))
        expected_weights = [(9,8),(9,8),(9,8),(10,8),(11,8),(9,9),(11,9),
                            (9,10),(11,10),(10,10),(10,10),(10,10),(10,10),
                            (10,10),(10,10),(10,10),(10,10),(10,10)]
        expected_weights.sort()
        self.ant.turn()
        ant_weights = self.ant.weights
        ant_weights.sort()
        self.assertEqual(ant_weights, expected_weights)

                
    def test_pre_turn_priorities_multiple_no_food(self):
        ''' Tests that when an ant has no food and is adjacent to a food,
            pheremones, and empty points that it priorites the next step in the
            following order. 
            
            priority food, pheremones, then empty
        '''
        
        self.ant.location = (98,2)
        self.world.addPheremone((98,1))
        self.world.addPheremone((98,1))
        expected_weights = [(97,1),(98,1),(98,1),(99,1),(98,1),(97,2),(97,3),
                            (98,3),(99,3),(99,2),(99,2),(99,2),(99,2),(99,2),
                            (99,2),(99,2),(99,2),(99,2)]   
        expected_weights.sort()
        self.ant.turn()
        ant_weights = self.ant.weights
        ant_weights.sort()
        self.assertEqual(ant_weights, expected_weights)
    
    
    def test_turn_with_food(self):
        ''' This test checks that the ant deposits a single pheremones at 
            current point when it has food.
        '''
        
        original_location = (50,50)
        self.ant.location = original_location
        self.ant.haveFood = True

        self.assertEqual(self.world.point(self.ant.location), None)
        self.ant.turn()
        self.assertEqual(self.world.point(original_location).totalPheremones(), 1)
       

    def test_turn_no_food(self):
        ''' Tests that an ant with no food makes no changes to it's current 
            point when it turns.
        '''
        
        self.assertTrue(False)
        
    
    def test_turn_with_food_hive(self):
        ''' This test checks that when an ant turns with food on a hive point 
            that it deposits the food at the hive.
        '''
         
        self.assertTrue(False)
        
    def test_chooseMove(self):
        ''' Tests the choose move function a move from the set generated.
        '''
        
        self.assertTrue(False)
        
    def test_turn_without_food_on_food(self):    
        ''' Tests that an ant without food on a food point picks up some food.
        '''
        
        self.ant.location = self.world.foodLocation 
     
        self.assertEqual(self.ant.location, self.world.foodLocation)
        self.assertEqual(self.ant.haveFood, False)

        self.ant.turn() # make ant take food

        self.assertEqual(self.ant.haveFood, True)
        self.assertEqual(self.world.food().foodLeft,self.world.totalFood - 1)

        new_location = self.ant.location

        self.assertTrue(False)
        
        
    def test_turn_with_food_on_food(self):    
        ''' Test that an ant with food on a food point does not pick up food.
        '''
        
        self.assertTrue(False)
        

    def test_post_turn(self):
        ''' Checks that an ant moves to the point that was chosen in pre_turn.
        '''
        
        self.assertEqual(self.ant.location, (10,10)) # match setup.
        self.ant.preTurn()
        nextLocation = self.ant.nextPoint
        self.ant.postTurn()
        self.assertEqual(self.ant.location, nextLocation)
   
    def test_drop_off_food(self):
        ''' XXX This needs to be broken up into two separate tests. Think I have
            already made them though
        '''

        self.ant.location = self.world.foodLocation 
     
        self.assertEqual(self.ant.location, self.world.foodLocation)
        self.assertEqual(self.ant.haveFood, False)

        self.ant.turn() # make ant take food

        self.assertEqual(self.ant.haveFood, True)
        self.assertEqual(self.world.food().foodLeft,self.world.totalFood - 1) 

        self.ant.location = self.world.hiveLocation 
        
        self.ant.turn() # make and drop off food
        
        self.assertEqual(self.ant.haveFood, False)
        self.assertEqual(self.world.hive().food,1) 
    
    
    def test_move(self):
        '''
        '''
        
        self.assertEqual(self.ant.location, self.world.hiveLocation)
        possible_moves = self.world.findNeighbours(self.ant.location) 
        
        self.ant.turn()
        
        self.assertEqual(self.ant.location in possible_moves, True)
        self.assertEqual(self.ant.lastPoint, self.world.hiveLocation)

        test_point = self.ant.location
        possible_moves = self.world.findNeighbours(self.ant.location) 
       
        self.ant.turn()
        
        self.assertEqual(self.ant.location in possible_moves, True)
        self.assertEqual(self.ant.lastPoint, test_point)


if __name__ == '__main__':
    unittest.main(verbosity=2)

