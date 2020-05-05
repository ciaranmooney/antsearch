class point(object):
    ''' A point in the world. This keeps track of the pheremone trails.
        or food, or hive.
    '''

    # XXX I reckon the point needs a .turn method to control pheremone decay

    def __init__(self, decay):
        ''' Creates an empty list for the pheremones whose size is equal to the
            number of steps required for decaying.
        '''

        self.pheremones  = []
        if decay == 0:
            self.pheremones = 0
        else:
            for i in range(decay):
                self.pheremones.append(0)

    def pheremoneDecay(self, step):
        ''' Sets a value of self.pheremones to zero to indicate decay of the
            pheremone trail.
        '''
        self.pheremones[(step-1) % len(self.pheremones)] = 0


    def pheremoneAdd(self, step):
        ''' Increments an entry in self.pheremones which contains the total
            pheremones added for each step.
        '''
        if isinstance(self.pheremones, int):
            self.pheremones = self.pheremones + 1
        else:
            self.pheremones[step % len(self.pheremones)] += 1


    def totalPheremones(self):
        ''' Inspects self.pheremone and gives an up-to-date total.
        '''
        runningTotal = 0

        if isinstance(self.pheremones, int):
            return self.pheremones
        else:
            for i in self.pheremones:
                runningTotal = runningTotal + i

            return runningTotal