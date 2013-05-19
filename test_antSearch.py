#! /usr/bin/env python

import unittest
import antSearch

class Simulation(unittest.TestCase):
    '''
    '''

    def setUp(self):
        pass

    def test_simulatin(self):
        ''' Create a 1x1 grid with food and hive in opposite corners. 
            Have one ant.

            Run Simulation.

            Check to see that food in hive is 1
            check to see food point is empty.
            check that one of the other diagonal points contains pheremones.
            Should only have 1 pheremone in that point

        '''
        fLoc = (1,1)
        hLoc = (0,0)
        self.world = antSearch.world(2, fLoc, hLoc)
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

        pheremones1 = self.world.point((1,0)).pheremones
        pheremones2 = self.world.point((0,1)).pheremones
        
        check = (pheremones1 == 1) or (pheremones2 == 1)

        self.assertTrue(check)

class TestPoint(unittest.TestCase):
    '''
    '''

    def setUp(self):
        '''
        '''
        self.p = antSearch.point()

    def test_create(self):
        '''
        '''
        self.p.pheremones = 0
       
    def test_pheremones(self):   
        '''
        '''
        self.p.pheremoneAdd()    
        self.assertEqual(self.p.pheremones, 1)
        self.p.pheremoneDecay()
        self.assertEqual(self.p.pheremones, 0)

class TestFood(unittest.TestCase):
    '''
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
    '''
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
    '''
    '''

    def setUp(self):
        '''
        '''
        self.find_neighbours_setUp()
    
    def find_neighbours_setUp(self):
        '''
        '''
        hiveLocation = (10,10)
        foodLocation = (99,2)
        self.World3 = antSearch.world(100, hive=hiveLocation, food=foodLocation)
    
    def test_create(self):
        '''
        '''
        World1 = antSearch.world(100)
        self.assertEqual(len(World1.world), 100)
        self.assertEqual(len(World1.world[0]), 100)

    def test_world_empty(self):
        '''
        '''
        p = self.World3.point((3,3))
        self.assertEqual(p, None)

    def test_create_food(self):
        '''
        '''
        newWorld = antSearch.world(100, food=(1,1))
        self.assertEqual(newWorld.point((12,13)), None)
        self.assertEqual(type(newWorld.point((1,1))), antSearch.food)
        food = newWorld.food()
        self.assertEqual(newWorld.point((1,1)).foodLeft, 100)
        self.assertEqual(newWorld.totalFood, 100)

        fLoc = (1,1)
        hLoc = (0,0)
        World2 = antSearch.world(2, fLoc, hLoc)
        
        self.assertEqual(type(World2.point(fLoc)), antSearch.food)
        self.assertEqual(type(World2.point(hLoc)), antSearch.hive)


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

    def test_turn_pheremone_decay(self):
        '''
        '''
        p = (21,10)

        for i in range(3):
            self.World3.addPheremone(p)
        
        self.assertEqual(self.World3.point(p).pheremones, 3) 

        self.World3.turn()

        self.assertEqual(self.World3.point(p).pheremones, 3) 

        for i in range(9):
            self.World3.turn()

        self.assertEqual(self.World3.point(p).pheremones, 2)

    def test_print_world(self):
        ''' World will have spaces where there are Nones,
        '''
        pass

    def test_pheremone_decay(self):
        '''
        '''
        foodLocation = (52,40)
        hiveLocation = (1,1)
        World2 = antSearch.world(100, food=foodLocation, hive=hiveLocation)
        
        coords = [(2,10),(10,2),(5,30),(55,21),(59,60),(82,15)]

        for i in coords:
            World2.addPheremone(i)

        for i in coords:
            self.assertEqual(World2.point(i).pheremones, 1)

        World2.pheremoneDecay()

        for i in coords:
            self.assertEqual(World2.point(i).pheremones, 0)
            
        World2.pheremoneDecay()

        for i in coords:
            self.assertEqual(World2.point(i).pheremones, 0)

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
        self.assertEqual(ant.objective, 'food')

    def test_leave_pheremone(self):
        '''
        '''
        ant = antSearch.ant(self.world)
        original_location = (50,50)
        ant.location = original_location
        ant.haveFood = True

        self.assertEqual(self.world.point(ant.location), None)

        ant.turn()

        self.assertEqual(self.world.point(original_location).pheremones, 1)
        
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
        self.assertEqual(ant.objective, 'food')
        self.assertEqual(ant.haveFood, False)

        ant.turn() # make ant take food

        self.assertEqual(ant.objective, 'hive')
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
        self.assertEqual(ant.objective, 'food')
        self.assertEqual(ant.haveFood, False)

        ant.turn() # make ant take food

        self.assertEqual(ant.objective, 'hive')
        self.assertEqual(ant.haveFood, True)
        self.assertEqual(self.world.food().foodLeft,self.world.totalFood - 1) 

        ant.location = self.world.hiveLocation 
        
        ant.turn() # make and drop off food

        self.assertEqual(ant.objective, 'food')
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
        '''
        '''
        ant = antSearch.ant(self.world) 
        ant.location = (10,9)
        ant.objective = "hive"

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

