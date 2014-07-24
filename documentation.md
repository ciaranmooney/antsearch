This document describes the behaviour of the various aspects of the antSearch simulation.

ant
===

Turn Behaviour
--------------
An Ants turn behaviour:
* if ant has no food, check to see on food point
* if ant has food then check to see if on hive 
* if ant has no food then look for pheremones or food 
** move (priority food, pheremones, then empty)
    
* if ant has food but not on food point then deposit pheremone 
** move (priority hive, pheremones, then empty)

pre-turn : search for neighbours and decide where to move
turn : deposit pheremones at current point, pick up food, or drop off 
    food
post-turn : move to next point previoulsy chosen

Move Behaviour
--------------

An ant remembers its last location and removes this as a choice for the next possible move.

When an ant searches around for another point to move to it will choose randomly but weight its decision based on whether the adjacent point contains food, pheremones or a hive. 

The last point that the ant was in is removed.
       

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
Pheremone decay
