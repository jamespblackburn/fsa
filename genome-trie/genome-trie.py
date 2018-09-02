# update trie implementation for python
import itertools as it

class Node():
    def __init__(self):
        self.children = {}
        self.accepts = False


def getTargets(target_file):
    root_node = Node()
    with open(target_file, 'r') as f:
        for line in f:
            buildTrie(line, root_node)


def buildTrie(target_string, root):
    current_node = root
    for char in target_string.strip():
        char = str(char).lower()
        if char not in current_node.children.keys():
            current_node.children[char] = Node()
        current_node = current_node.children[char]
    current_node.accepts = True


if __name__ == "__main__":
    getTargets('test_sequence.txt')