# Implementation of deterministic and non-deterministic finite state machines.

import os
import json

class State():
    #docstring
    def __init__(self, id_number, exits={}, starts=False, accepts=False):
        # exits: dict with char keys and state id_number values.
        self.id_number = id_number
        self.starts = starts
        self.accepts = accepts
        self.exits = exits
    
    def __str__(self):
        as_string = str(self.id_number)
        as_string += " start_state={}".format(self.starts)
        as_string += " accept_state={}".format(self.accepts)
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
            
