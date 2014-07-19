Turn based behaviour of ant search

ant
===
pre-turn : search for neighbours and decide where to move
turn : deposit pheremones at current point, pick up food, or drop off 
    food
post-turn : move to next point previoulsy chosen

world
=====
pre-turn: check to see if simulation has finished, call all ants.pre-turn()
turn: phermeones decay, call all ants.turn()
post-turn: call all ants.post_turn(), increment step counter by one


