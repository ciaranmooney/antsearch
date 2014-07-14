#! /usr/bin/env python

import unittest
import antSearch

class Simulation(unittest.TestCase):
    '''
    '''

    def setUp(self):
        '''
        '''
        pass

    def test_simulation(self):
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
       
        food = self.world.food()
        food.foodLeft = 1
        self.world.totalFood = 1

        self.assertEqual(self.world.food(), food)
        self.assertEqual(type(self.world.hive()), antSearch.hive)

        self.assertEqual(self.world.hive().food, 0)
        self.assertEqual(self.world.food().foodLeft, 1)
        
        sim = antSearch.simulation(self.ants, self.world)

        sim.run()

        self.assertEqual(self.world.hive().food, 1)
        self.assertEqual(self.world.food().foodLeft, 0)

        print(self.world.pheremones)
        self.assertTrue(len(self.world.pheremones) > 0)

class TestPoint(unittest.TestCase):
    ''' Tests for the Point Class
    ''' 

    def setUp(self):
        ''' Creates new point for each test.
        '''
        
        self.p = antSearch.point()
       
    def test_new_pheremone_zero(self):   
        ''' Tests that when a point is created that it has no 
            pheremones.
        '''
        self.assertEqual(self.p.totalPheremones(), 0)
        self.assertNotEqual(self.p.totalPheremones(), -1)
        self.assertNotEqual(self.p.totalPheremones(), 1)
        
    def test_addPheremones(self):
        ''' Tests new point has no pheremones, the has pheremones and step when
            point.pheremoneAdd(step) is called.
            
            Checks that a new phermeone with a new step value is added if a
            different step value is given.
        '''
                
        self.assertEqual(self.p.totalPheremones(), 0)
        
        self.p.pheremoneAdd(1)  # one step
        
        self.assertEqual(self.p.pheremones, {1:1})
        
        self.p.pheremoneAdd(2) # two steps
        
        self.assertEqual(self.p.pheremones, {1:1,2:1})
        
        
    def test_totalPheremones(self):
        ''' Checks that the totalPheremones method of point is working properly.
        
            Checks that a two pheremoneAdds on the same step increase total, and
            another pheremoneAdd on another step increases total.
            
        '''
        self.assertEqual(self.p.totalPheremones(), 0)
        
        self.p.pheremoneAdd(1)  # pheremone at step one
        
        self.assertEqual(self.p.totalPheremones(), 1)
        self.assertNotEqual(self.p.totalPheremones(), 2)
        self.assertNotEqual(self.p.totalPheremones(), 0)
        self.assertNotEqual(self.p.totalPheremones(), -1)

        self.p.pheremoneAdd(1) # Another pheremone at step one
        
        self.assertEqual(self.p.totalPheremones(), 2)
        self.assertNotEqual(self.p.totalPheremones(), 3)
        self.assertNotEqual(self.p.totalPheremones(), 1)
        self.assertNotEqual(self.p.totalPheremones(), -1)
        
        self.p.pheremoneAdd(2) # pheremone at step two
        
        self.assertEqual(self.p.totalPheremones(), 3)
        self.assertNotEqual(self.p.totalPheremones(), 4)
        self.assertNotEqual(self.p.totalPheremones(), 2)
        self.assertNotEqual(self.p.totalPheremones(), -1)
        self.assertNotEqual(self.p.totalPheremones(), 0)
        
        
    def test_multiple_addPheremones(self):
        ''' Tests for when multiple ants add pheremones in the the same turn.
            This will mean the corresponding tuple in point.pheremones will have
            mutliple pheremones for a step.
        '''
        self.assertEqual(self.p.totalPheremones(), 0)
        self.p.pheremoneAdd(1)  # first pheremone added in step 1
        self.p.pheremoneAdd(1)  # second pheremone added in step 1
        
        self.assertEqual(self.p.pheremones, {1:2})
        
    def test_pheremoneDecay(self):
        ''' Tests when a point is created it has no pheremones. 
            Then adds pheremones and checks it decays to zero but not below.            
        '''
        
        self.assertEqual(self.p.totalPheremones(), 0)
        self.p.pheremoneAdd(1)  # step 1
        self.assertEqual(self.p.totalPheremones(), 1)
        self.p.pheremoneDecay()
        self.assertEqual(self.p.totalPheremones(), 0)
        self.p.pheremoneDecay()
        self.assertEqual(self.p.totalPheremones(), 0)
        self.assertNotEqual(self.p.totalPheremones(), -1)
        
    def test_pheremoneDecay_rate_different(self):
        ''' Tests that different pheremones on the same point will decay
            at different times depending on when they were added.
        '''
        self.assertTrue(False)

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
        '''
        '''
        centre1 = (11,34)
        n_sol = [(10,35),(11,35),(12,35),(10,34),(12,34),(10,33),(11,33),(12,33)]
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
        self.assertEqual(self.World3.point(point).pheremones, 1)
        self.World3.addPheremone(point)
        self.assertEqual(self.World3.point(point).pheremones, 2)
        
        self.assertEqual(self.World3.pheremones, [point])
    
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
        self.assertEqual(self.World3.point(point).pheremones, 1)
        self.World3.removePheremone(point)
        self.assertEqual(self.World3.point(point).pheremones, 0)

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

    def test_pheremoneDecay(self):
        ''' Tests that pheremoneDecay method reduces a number of 
            different points pheremone count by one. Also checks that
            pheremonedecay method does not go below zero.
            
        '''
        coords = [(2,10),(10,2),(5,30),(55,21),(59,60),(82,15)]
        
        for i in coords:
            self.World3.addPheremone(i)

        for i in coords:
            self.assertEqual(self.World3.point(i).pheremones, 1)

        self.World3.pheremoneDecay()

        for i in coords:
            self.assertEqual(self.World3.point(i).pheremones, 0)
            
        self.World3.pheremoneDecay()

        for i in coords:
            self.assertEqual(self.World3.point(i).pheremones, 0)
        
    def test_pheremoneDecay_rate(self):
        ''' Checks that the pheremone decay of a world happens at the 
            rate specific (ie per number of turns)
        '''
        
        # Each pheremone has a slightly different decay time as it will
        # depend on when it is depositied.
        
        check = False
        self.assertTrue(check)
        
        coords = [(2,10),(10,2),(5,30),(55,21),(59,60),(82,15)]

        for i in coords:
            self.World3.addPheremone(i)
        
        for i in coords:
            self.assertEqual(self.World3.point(i).pheremones, 1)
        
        self.World3.turn()
        
        for i in coords:
            self.assertEqual(self.World3.point(i).pheremones, 1)
            
        while self.World3.steps < 10:
            self.World3.turn()
        
        for i in coords:
            self.assertEqual(self.World3.point(i).pheremones, 0)
            
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

        self.assertEqual(self.World3.point((1,1)).pheremones, 1)

        self.World3.pheremoneDecay()
        
        self.assertEqual(self.World3.point((1,1)).pheremones, 0)
        self.assertTrue((1,1) not in self.World3.pheremones)

        self.assertTrue(False)
        
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
    '''
    '''

    def setUp(self):
        '''
        '''
        hiveLocation = (10,10)
        foodLocation = (99,2)
        self.world = antSearch.world(100, hive=hiveLocation, food=foodLocation)

    def test_init(self):
        '''
        '''
        ant = antSearch.ant(self.world)

        self.assertEqual(ant.world, self.world)
        self.assertEqual(ant.haveFood, False)
        self.assertEqual(ant.location, self.world.hiveLocation)

    def test_leave_pheremone(self):
        '''
        '''
        ant = antSearch.ant(self.world)
        original_location = (50,50)
        ant.location = original_location
        ant.haveFood = True

        self.assertEqual(self.world.point(ant.location), None)

        ant.turn()

        self.assertEqual(self.world.point(original_location).totalPheremones(), 1)
        
    def test_turn(self):
        '''
        '''
        ant = antSearch.ant(self.world) 
        
        self.assertEqual(ant.location, self.world.hiveLocation)
        possible_moves = self.world.findNeighbours(ant.location) 

        ant.turn()
        self.assertEqual(ant.location in possible_moves, True)
   
    def test_turn_pheremone(self):
        '''
        '''
        ant = antSearch.ant(self.world) 
        ant.location = (50,50)
        self.world.addPheremone((49,49)) 
        
        possible_moves = self.world.findNeighbours(ant.location) 
        possible_moves.append((49,49))
        possible_moves.sort()
        ant.turn()
        self.assertEqual(ant.__moves__, possible_moves)
        self.assertEqual(ant.location in possible_moves, True)

    def test_turn_food(self):
        '''
        '''
        ant = antSearch.ant(self.world) 
        ant.location = (98,2) # one away from food
        
        possible_moves = self.world.findNeighbours(ant.location)
        for each in range(len(possible_moves)):
            possible_moves.append(self.world.foodLocation)
        
        possible_moves.sort()
        ant.turn()
        self.assertEqual(ant.__moves__, possible_moves)
        self.assertEqual(ant.location in possible_moves, True)
   
    def test_picked_up_food(self):
        '''
        '''
        ant = antSearch.ant(self.world) 
        ant.location = self.world.foodLocation 
     
        self.assertEqual(ant.location, self.world.foodLocation)
        self.assertEqual(ant.haveFood, False)

        ant.turn() # make ant take food

        self.assertEqual(ant.haveFood, True)
        self.assertEqual(self.world.food().foodLeft,self.world.totalFood - 1)

        new_location = ant.location

        self.assertNotEqual(ant.location, self.world.foodLocation)
        ant.turn()

        self.assertEqual(self.world.point(new_location).pheremones, 1)

    def test_drop_off_food(self):
        '''
        '''
        ant = antSearch.ant(self.world) 
        ant.location = self.world.foodLocation 
     
        self.assertEqual(ant.location, self.world.foodLocation)
        self.assertEqual(ant.haveFood, False)

        ant.turn() # make ant take food

        self.assertEqual(ant.haveFood, True)
        self.assertEqual(self.world.food().foodLeft,self.world.totalFood - 1) 

        ant.location = self.world.hiveLocation 
        
        ant.turn() # make and drop off food
        
        self.assertEqual(ant.haveFood, False)
        self.assertEqual(self.world.hive().food,1) 
    
    def test_turn_hive_no_food(self):
        '''
        '''
        ant = antSearch.ant(self.world) 
        ant.location = (10,9)
        
        possible_moves = self.world.findNeighbours(ant.location)
        possible_moves.sort()
        ant.turn()
        self.assertEqual(ant.__moves__, possible_moves)
        self.assertEqual(ant.location in possible_moves, True)
    
    def test_turn_hive_with_food(self):
        ''' Tests that the possible moves for an ant with food are 
            correctly weighted given that the hive is next to the ant.
        '''
        ant = antSearch.ant(self.world)
        ant.location = (10,9)
        ant.haveFood = True
        
        possible_moves = self.world.findNeighbours(ant.location)
        for each in range(len(possible_moves)):
            possible_moves.append(self.world.hiveLocation)
        possible_moves.sort()
        ant.turn()
        
        self.assertEqual(ant.__moves__, possible_moves)
        self.assertEqual(ant.location in possible_moves, True)
    
    def test_move(self):
        '''
        '''
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

if __name__ == '__main__':
    unittest.main(verbosity=2)

