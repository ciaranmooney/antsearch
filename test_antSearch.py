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
        assert sim.complete, True
        assert sim.success, True

    def test_small_world(self):
        sim = simulation()
        world_dimensions = [1, 1]
        w = world(world_dimensions)
        sim.build(w)
        assert sim.world.size == 1
        assert sim.world.x == 1
        assert sim.world.y == 1
        assert sim.world.world == [1,1]