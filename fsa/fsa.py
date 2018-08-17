# Implementation of deterministic and (TODO) non-deterministic finite state machines.

import os
import json

class State():
    """Represents a unique state within a finite state automaton.
    
    Attributes:
        id (int): The unique integer identifier of this state.
        starts (bool): True if this is the start state; False if not.
        accepts (bool): True if this state accepts; False if not.
        arcs (dict): A dictionary with a symbol as key and a tuple of
                     (destination, probability) as values.
                     destination is another State instance; probability
                     is a float from (0.0 - 1.0].
                     TODO: implement normalization for probabilities that do
                     not sum to 1 or arcs whose probabilities are not between
                     0 and 1.
    """
    
    def __init__(self, id, arcs={}, starts=False, accepts=False):
        
        self.id = id
        self.starts = starts
        self.accepts = accepts
        self.arcs = arcs

    def __str__(self):
        # docstring: basically print out a row of the fsa's transition table.
        as_string = str("q" + str(self.id))
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
            return self.id == other.id
        except AttributeError:
            return False

    def __hash__(self):
        return hash(self.id)


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
            if input_string[i] not in current_state.arcs.keys():
                return False
            current_state = current_state.arcs[input_string[i]][0]
            i += 1
        if current_state.accepts:
            return True
        return False

# The following builds an FSA that will accept *only* the input "abc".
# More complex FSA's to follow...
# also TODO is move these over to unit testing.

q0 = State(0, starts=True, accepts=False)
q1 = State(1, starts=False, accepts=False)
q2 = State(2, starts=False, accepts=False)
q3 = State(3, starts=False, accepts=True)

q0.arcs = {'a':(q1, 1)}
q1.arcs = {'b':(q2, 1)}
q2.arcs = {'c':(q3, 1)}

# try adding an arc to expand the set of accepted strings?

q2.arcs['q'] = (q3, 1)

fsa = Automaton([q0, q1, q2, q3])

for string in ['a', 'ab', 'abc', 'cba', 'ac', 'aaa', 'abc', 'abcd', 'abq']:
    print(string + ": " + str(fsa.recognize(string)))