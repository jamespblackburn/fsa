# Implementation of deterministic and non-deterministic finite state machines.

import os
import json

class State():
    #docstring
    def __init__(self, id_number, reachable_states={}, starts=False, accepts=False):
        
        # reachable_states = dict, key is destination state, value is tuple (symbol, probability)

        self.id_number = id_number
        self.starts = starts
        self.accepts = accepts
        self.reachable_states = reachable_states
    
    def __str__(self):
        as_string = str("q" + str(self.id_number))

        for next_state in self.reachable_states.keys():
            as_string += " --> " +\
                         "q" + str(next_state) +\
                         "\tsymbol=" +\
                         str(self.reachable_states[next_state][0]) +\
                         "\tprob=" +\
                         str(self.reachable_states[next_state][1])
                         
        return as_string


class Automaton():
    def __init__(self, states):
        self.state_set = set()
        for state in states:
            self.state_set.add(state)

    def __str__(self):
        as_string = ""
        for state in self.state_set:
            as_string += str(state) + "\n"
        return as_string.strip()

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


q0 = State(0, {1:('a', 1)}, starts=True, accepts=False)
q1 = State(1, {2:('b', 1)}, starts=False, accepts=False)
q2 = State(2, {3:('c', 1)}, starts=False, accepts=True)

fsa = Automaton([q0, q1, q2])
print(fsa)