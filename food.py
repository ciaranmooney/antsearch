class food(object):
    ''' Food object. Keeps track of how much food is left.
    '''
    def __init__(self, amount=100):
        '''
        '''

        self.foodLeft = amount


    def removeFood(self):
        '''
        '''

        self.foodLeft -= 1