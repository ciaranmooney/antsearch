class hive(object):
    ''' Hive object, keeps track of how much food is collected. So that we can
        figure out if we have reached the end of the simulation.
    '''

    def __init__(self,):
        '''
        '''

        self.food = 0


    def addFood(self):
        '''
        '''

        self.food += 1