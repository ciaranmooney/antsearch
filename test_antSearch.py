# Copyright 2013,2014 Ciarán Mooney (general.mooney@googlemail.com)

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from simulation import simulation
from world import world


class Simulation(unittest.TestCase):
    
    def test_empty_simulation(self):
        sim = simulation()
        w = world()
        sim.build(w)
        sim.run()
        self.assertTrue(sim.complete)
        self.assertTrue(sim.success)

    def test_small_world(self):
        world_dimensions = (1, 1)
        w = world(world_dimensions)
        sim = simulation()
        sim.build(w)
        self.assertEqual(sim.world.size, 1)
        self.assertEqual(sim.world.x, 1)
        self.assertEqual(sim.world.y, 1)
        self.assertEqual(sim.world.world, (1,1))