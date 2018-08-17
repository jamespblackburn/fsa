# Implementation of deterministic and (TODO) non-deterministic finite state machines.

import os
import json
import logging

input_log = logging.Logger(name='parse input', level='INFO')


class Automaton():
    
    def __init__(self, fsa_file):
        
        # Init fields
        self.start_states, self.accept_states = [], []
        self.trans_table = {}

        with open(fsa_file, 'r') as fsa:
            data = [ line.split() for line in fsa.readlines() ]
            for item in data:
                if item[0].strip() not in ['$', '@']:
                    self.add_transition(data)
                else:
                    self.set_special_states(item[1:], item[0])
        print(self)


    def __str__(self):
        as_string = ""
        for state in self.state_set:
            as_string += str(state) + "\n"
        return as_string.strip()


    def set_special_states(self, state_list, key):
        self.start_states = [ _ for _ in state_list if key=='$' ]
        self.accept_states = [ _ for _ in state_list if key=='@' ]


    def add_transition(self, data):
        if len(data) != 4:
            input_log.warning("Malformed transition data: ignoring this line")
            return 1
        orig, dest, sym = data[0], data[1], data[2]
        try:
            prob = float(data[3])
        except ValueError or IndexError:
            input_log.warning("Invalid probability value: defaulting to 1.0")
            prob = 1.0
        self.trans_table[sym] = {'orig':orig,
                                 'dest':dest,
                                 'sym':sym,
                                 'prob':prob
                                 }
        return 0

    def recognize(self, input_string):    
        pass

auto = Automaton("test.fsa")