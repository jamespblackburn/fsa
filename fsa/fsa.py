# Implementation of deterministic and non-deterministic finite state machines.

import os
import json

class State():
    #docstring
    def __init__(self, number, starts=False, accepts=False):
        self.number = number
        self.starts = starts
        self.accepts = accepts
    
    def __str__(self):
        as_string = str(self.number)
        as_string += " start_state={}".format(self.starts)
        as_string += " accept_state={}".format(self.accepts)
        return as_string

class Transition():
    #docstring
    def __init__(self, start, end, symbol, prob=1):
        self.start = start
        self.end = end
        self.symbol = symbol
        self.prob = prob
    
    def __str__(self):
        as_string = str(self.start) + " -> " + str(self.end)
        as_string += ' symbol={}'.format(self.symbol)
        as_string += ' probability={}'.format(self.prob)
        return as_string

class Automaton():
    def __init__(self, states, transitions):
        self.state_set = set()
        self.trans_table = []
        self.as_string = ""
        self.start_state = None
        self.accept_states = set()

        for state in states:
            self.state_set.add(state)
            if state.starts:
                self.start_state = state
            if state.accepts:
                self.accept_states.add(state)
        
        for transition in transitions:
            self.trans_table.append(transition)

    def __str__(self):
        for state in self.state_set:
            self.as_string += str(state) + "\n"
        for transition in self.trans_table:
            self.as_string += str(transition) + "\n"
        return self.as_string.strip()

    def recognize(self, input_string):
        # docstring: returns True if string is recognized, otherwise False
        
        i = 0
        current_state = self.start_state

        while i < len(input_string):
            is_legal = self.legal_moves(current_state, input_string[i])
            if is_legal == []:
                return False
            else:
                current_state = is_legal[0].end
                i += 1
        if current_state.accepts:
            return True
        return False

    def legal_moves(self, current_state, current_char):
        moves = []
        for t in self.trans_table:
            if t.start == current_state and t.symbol == current_char:
                moves.append(t)
        return moves

        
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
            

states = [State(0, starts=True),
          State(1),
          State(2),
          State(3, accepts=True)]
trans = [Transition(0, 1, 'a'),
         Transition(1, 2, 'b'),
         Transition(2, 3, 'c'),
         Transition(3, 4, 'd')]

fsa = Automaton(states, trans)

print(fsa)

print(fsa.recognize('abcd'))
print(fsa.recognize('bcd'))
