# Implementation of deterministic and (TODO) non-deterministic finite state machines.

import os
import json
import logging
import re
import pdb

input_log = logging.Logger(name='parse input', level='DEBUG')


class Automaton():
    
    def __init__(self, fsa_file):
        
        # Init fields
        self.trans_table = {}
        self.states = {}

        with open(fsa_file, 'r') as fsa:
            line_num = 0
            for line in fsa.readlines():
                line_num += 1
                transition = re.split("[,:\s]", line.strip())
                if transition[0] in ["accept", "start"]:
                    self.update_states(transition[1:], transition[0])
                else:
                    try:
                        orig = int(transition[0])
                        dest = int(transition[1])
                        symb = str(transition[2])
                        prob = float(transition[3])
                    except ValueError:
                        input_log.error("Invalid data in line {}".format(line_num))
                        continue
                    t_key = len(self.trans_table)
                    t_val = [orig, dest, symb, prob]
                    self.trans_table[t_key] = t_val
                    self.states[orig] = { "start": 0.0, "accept": 0.0}
                    self.states[dest] = { "start": 0.0, "accept": 0.0}

    def update_states(self, input_list, function):
        i = 0
        while i < len(input_list):
            state = int(input_list[i])
            prob = float(input_list[i+1])
            self.states[state][function] = prob
            i += 2

    def __str__(self):
        as_string = ""
        for t in self.trans_table.keys():
            as_string += "transition {}: " \
                         "from {} to {} on symbol {} with probability {}\n" \
                         .format(t,
                                 self.trans_table[t][0],
                                 self.trans_table[t][1],
                                 self.trans_table[t][2],
                                 self.trans_table[t][3]
                                )
        return as_string.strip()


    def recognize(self, input_string):    
        
        input_string = list(input_string)
        input_string.reverse()
        for s in self.states:
            if self.states[s]["start"] == 1.0:
                current_state = s

        print(current_state)
        #pdb.set_trace()
        while input_string:
            for t in self.trans_table:
                current_sym = input_string.pop()
                if self.trans_table[t][2] == current_sym:
                    print("match from state {} on symbol {}".format(current_state, current_sym))
                    current_state = self.trans_table[t][1]
                    print("new current state is {}".format(current_state))
                else:
                    return 1 # no arcs out of current state for current symbol
        
        if self.states[current_state]['accept']==1.0:
            return 0 # accepted
        return 2 # string parsed completely but ended on a non-accepting state


auto = Automaton("test.fsa")
print(auto)
print(auto.recognize('abcd'))