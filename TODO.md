TODO
=====

- [ ] Write a 1x1, 2x1 and 3x1 1D simulation.
- [ ] Re-read and comment all tests
- [ ] Re-write tests to use the "setUP" function rather than creating new
    worlds each time.
- [ ] Write food class - unnecessary
- [ ] Write PyGame visuatilsation
- [ ] Write style guide. One line between ''' ''' and code, two lines between
    different function.
- [ ] There should be pre-step, step, post-step functions for points, ants and 
    the world.
- [ ] Document counting from zero.
- [ ] Re-write fragile tests.
- [ ] ant.move(): The weighting of pheremones will give a weighting to a point
     with zero pheremones due to totalPheremones()+1.
- [x] Make pheremones decay "independantly" depending on when they were
      deposited.
- [x] Decay should be a rate, need a step counter of world.
