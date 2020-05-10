# Copyright 2020 Ciarán Mooney (admin@cmooney.co.uk)

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class participantInterface:
    """
    An interface to define the behaviours of the simulation participants.
    Each participant should implement the following functions:

    * survey
    * decide
    * act
    * resolve
    """
    def survey(self):
        """"""
        pass

    def decide(self):
        pass

    def act(self):
        pass

    def resolve(self):
        pass