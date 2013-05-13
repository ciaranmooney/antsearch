#! /usr/bin/env python

import unittest
import antSearch

class TestPoint(unittest.TestCase):
    
    def setUp(self):
        self.p = antSearch.point()

    def test_create(self):
        self.p.pheremones = 0
       
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

    def test_world_empty(self):
        p = self.World3.point((3,3))
        self.assertEqual(p, None)

    def test_create_food(self):
        newWorld = antSearch.world(100, food=(1,1))
        self.assertEqual(newWorld.point((12,13)), None)
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

    def test_addPheremone(self):
        point = (49,49)
        self.assertEqual(self.World3.point(point), None)
        self.World3.addPheremone(point)
        self.assertEqual(self.World3.point(point).pheremones, 1)

    def test_removePheremone(self):
        point = (50,50)
        self.assertEqual(self.World3.point(point), None)
        self.World3.addPheremone(point)
        self.assertEqual(self.World3.point(point).pheremones, 1)
        self.World3.removePheremone(point)
        self.assertEqual(self.World3.point(point).pheremones, 0)

class TestAnt(unittest.TestCase):
    
    def setUp(self):
        hiveLocation = (10,10)
        foodLocation = (99,2)
        self.world = antSearch.world(100, hive=hiveLocation, food=foodLocation)

    def test_init(self):
        ant = antSearch.ant(self.world)

        self.assertEqual(ant.world, self.world)
        self.assertEqual(ant.haveFood, False)
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
        self.world.addPheremone((49,49)) 
        
        possible_moves = self.world.findNeighbours(ant.location) 
        possible_moves.append((49,49))
        possible_moves.sort()
        ant.turn()
        self.assertEqual(ant.__moves__, possible_moves)
        self.assertEqual(ant.location in possible_moves, True)

    def test_turn_food(self):
        ant = antSearch.ant(self.world) 
        ant.location = (98,2)
        
        possible_moves = self.world.findNeighbours(ant.location)
        for each in range(len(possible_moves)):
            possible_moves.append(self.world.foodLocation)
        
        possible_moves.sort()
        ant.turn()
        self.assertEqual(ant.__moves__, possible_moves)
        self.assertEqual(ant.location in possible_moves, True)
   
    def test_picked_up_food(self):
        ant = antSearch.ant(self.world) 
        ant.location = self.world.foodLocation 
     
        self.assertEqual(ant.location, self.world.foodLocation)
        self.assertEqual(ant.objective, 'food')
        self.assertEqual(ant.haveFood, False)

        ant.turn() # make ant take food

        self.assertEqual(ant.objective, 'hive')
        self.assertEqual(ant.haveFood, True)
        self.assertEqual(self.world.food().foodLeft,self.world.totalFood - 1) 

    def test_drop_off_food(self):
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
        ant = antSearch.ant(self.world) 
        ant.location = (10,9)
        
        possible_moves = self.world.findNeighbours(ant.location)
        possible_moves.sort()
        ant.turn()
        self.assertEqual(ant.__moves__, possible_moves)
        self.assertEqual(ant.location in possible_moves, True)
    
    def test_turn_hive_with_food(self):
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

