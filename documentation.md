This document describes the behaviour of the various aspects of the antSearch simulation.

ant
===

Turn Behaviour
--------------
pre-turn : search for neighbours and decide where to move
turn : deposit pheremones at current point, pick up food, or drop off 
    food
post-turn : move to next point previoulsy chosen

Priorties
---------

When an ant searches around for another point to move to it will choose randomly but weight its decision based on whether the adjacent point contains food, pheremones or a hive. 

world
=====

Turn Behaviour
--------------
pre-turn: check to see if simulation has finished, call all ants.pre-turn()
turn: phermeones decay, call all ants.turn()
post-turn: call all ants.post_turn(), increment step counter by one


points
======

Turn Behaviour
--------------

