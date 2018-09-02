# Implementation of deterministic and (TODO) non-deterministic finite state machines.

import os
import json
import logging
import re
import pdb

input_log = logging.Logger(name='parse input', level='ERROR')


class Automaton():
    
    def __init__(self, fsa_file):
        self.trans_table = {}
        self.start_states = {}
        self.accept_states = {}
        try:
            self.parse_file(fsa_file)
        except FileNotFoundError:
            print("File {} not found.").format(fsa_file)

    def __str__(self):
        as_string = ""
        for t in self.trans_table.keys():
            as_string +=
                "transition {}: " \
                "from {} to {} on symbol {} with probability {}\n" \
                .format(t,
                 self.trans_table[t][0],
                 self.trans_table[t][1],
                 self.trans_table[t][2],
                 self.trans_table[t][3])
        return as_string.strip()

    def parse_file(self, filename, verbose=False):
        """
        Parse a .fsa file. If the file is not in the correct format,
        it will not be parsed properly and errors will be logged.

        Arguments:
        filename -- the file to be parsed.
        verbose -- whether to output information as the method runs.
        """
        with open(filename, 'r') as fsa:
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

    def update_states(self, input_list, function):
        
        """
        Update the states dictionaries with information about starting
        and accepting states.

        Arguments:
        input_list -- a list of alternating state numbers and
        probabilities.
        function -- whether this information is for 'start' or
        'accept' values.
        """

        i = 0
        while i < len(input_list):
            state = int(input_list[i])
            prob = float(input_list[i+1])
            target_dict = getattr(self, function+'_states')
            target_dict[state] = prob
            i += 2

    def traverse(self, input_string):
        """
        Test whether an input string is accepted by the automaton.

        Arguments:
        input_string -- the string to be parsed.
        """
        
        current_state = 0 # for now... this will turn into a stack later
        probability = 1.0

        #pdb.set_trace()
        for sym in input_string:
            for t in self.trans_table:
                if sym == self.trans_table[t][2]:
                    current_state = self.trans_table[t][1]
                    probability *= self.trans_table[t][3]
                    break # this will also turn into a stack
            else:
                return None
            
        if current_state in self.accept_states:
            print(input_string, "[{}]".format(probability))
        return None


if __name__ == "__main__":
    auto = Automaton("test.fsa")
    for string in ['ab', 'abcd', 'abc', 'abcde']:
        auto.traverse(string)