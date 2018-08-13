# Implementation of deterministic and non-deterministic finite state machines.

import os
import json

class State():
    #docstring
    def __init__(self, id_number, arcs={}, starts=False, accepts=False):
        
        # reachable_states = dict, key is arc symbol, value is tuple (destination, probability)

        self.id_number = id_number
        self.starts = starts
        self.accepts = accepts
        self.arcs = arcs

    def __str__(self):
        # docstring: basically print out a row of the fsa's transition table.
        as_string = str("q" + str(self.id_number))
        for arc in self.arcs:
            as_string += " --> " +\
                         "q" + str(self.arcs[arc][0]) +\
                         "\tsymbol=" +\
                         str(arc) +\
                         "\tprob=" +\
                         str(self.arcs[arc][1])
        return as_string
    
    def __eq__(self, other):
        try:
            return self.id_number == other.id_number
        except AttributeError:
            return False

    def __hash__(self):
        # try this first
        return hash(self.id_number)

    def get_arcs(self):
        # returns tuple of tuples: (destination_state, probability)
        pass


class Automaton():

    def __init__(self, states):
        self.state_set = set()
        self.start_state = None
        self.accept_states = set()
        
        for state in states:
            self.state_set.add(state)
            if state.starts:
                self.start_state = state
            if state.accepts:
                self.accept_states.add(state)

    def __str__(self):
        as_string = ""
        for state in self.state_set:
            as_string += str(state) + "\n"
        return as_string.strip()

    def recognize(self, input_string):
        current_state = self.start_state
        if current_state == None:
            print("Error: no start state found in this automaton.")
            return False
        i = 0
        while i < len(input_string):
            if not current_state.reachable_states:
                return False
            if input_string[i] != current_state.reachable_states[1][0]:
                continue

        
        # pseudocode
        # while i < len(input_string)
            # Get the start state and make it current_state.
            # Find all transitions in the transition table that start with it.
            # Check to see if any of these arcs lead out on the character at index i.
            # If yes: current state becomes the out state from that transition. Increment i.
            # If no: return False.
        # after loop exits: does our current state accept?
            # If yes, return True
            # If no, return False


q0 = State(0, {'a':(1, 1)}, starts=True, accepts=False)
q1 = State(1, {'b':(2, 1)}, starts=False, accepts=False)
q2 = State(2, {'c':(3, 1)}, starts=False, accepts=False)
q3 = State(3, None, starts=False, accepts=True)

fsa = Automaton([q0, q1, q2])
print(fsa)