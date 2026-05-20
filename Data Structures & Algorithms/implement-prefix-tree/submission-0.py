class Node:
    def __init__(self,val = None):
        self.children = {}

class PrefixTree:
    # it's natrual to use a graph structure because we want to support quick prefix search
    # One node class is nessary, and it should have a value and a list of its children  
    # for init, we create the first node, the first node has no val and an empty children list
    # when insert, we parse the word char by char, each char, we first check if it exist in this level, if not, we create a new node, if it has, we acess the next node and do it again
    # for serach, I guess it looks for exact mathching, so we retrival graph by look up the char one by one
    # one problem here is, for exact match, we need to make sure we distinguish it with prefix search, so adding an end node or something might help, or we can have another hashset to handle this seperatly 
    # one thing I found is a children list is not enogh, becasue we need two operation, 1. loop up children, 2. go to the child node, so probably a map with {char: node} structure
    # we have never used the self.val for node, because we always check the current char in the prev level
    def __init__(self):
        self.lookup = set()
        self.trie = Node()

    def insert(self, word: str) -> None:
        self.lookup.add(word)
        curr = self.trie
        for char in word:
            ## TODO, refine logic
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = Node()
                curr = curr.children[char]
           


    def search(self, word: str) -> bool:
        return word in self.lookup
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True
        