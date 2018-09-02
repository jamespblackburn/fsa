# update trie implementation for python
import itertools as it

class Node():
    def __init__(self):
        self.children = {}
        self.accepts = False


def getTargets(target_file, root):
    with open(target_file, 'r') as f:
        for line in f:
            buildTrie(line, root)


def buildTrie(target_string, root):
    current_node = root
    for char in target_string.strip():
        char = str(char).lower()
        if char not in current_node.children.keys():
            current_node.children[char] = Node()
        current_node = current_node.children[char]
    current_node.accepts = True


def traverse(input_string, root_node):
    current_node = root_node
    i, j = 0, 0
    while j < len(input_string):
        if input_string[j] in current_node.children.keys():
            current_node = current_node.children[input_string[j]]
            j += 1
        else:
            i += 1
            j = i
            current_node = root_node       
        if current_node.accepts:
            print('found sequence {}'.format(input_string[i:j]))
                        

if __name__ == "__main__":
    root_node = Node()
    getTargets('test_sequence.txt', root_node)
    with open('test_genome.txt', 'r') as genome:
        for line in genome:
            traverse(line, root_node)