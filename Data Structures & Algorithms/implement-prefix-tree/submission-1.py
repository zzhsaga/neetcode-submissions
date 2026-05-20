class Node:
    def __init__(self,is_end = False):
        self.children = {}
        self.is_end = is_end

class PrefixTree:
    # it's natrual to use a graph structure because we want to support quick prefix search
    # One node class is nessary, and it should have a value and a list of its children  
    # for init, we create the first node, the first node has no val and an empty children list
    # when insert, we parse the word char by char, each char, we first check if it exist in this level, if not, we create a new node, if it has, we acess the next node and do it again
    # for serach, I guess it looks for exact mathching, so we retrival graph by look up the char one by one
    # one problem here is, for exact match, we need to make sure we distinguish it with prefix search, so adding an end node or something might help, or we can have another hashset to handle this seperatly 
    # one thing I found is a children list is not enogh, becasue we need two operation, 1. loop up children, 2. go to the child node, so probably a map with {char: node} structure
    # we have never used the self.val for node, because we always check the current char in the prev level
    # if we dont want to bypasas the trie search, we can use a bool to identify if current node is previous end char
    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            ## TODO, refine logic
            if char not in curr.children:
                 curr.children[char] = Node()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True

# we can furthere reduce the logic in search and startsWith because they sharing hte traverse process, it should take a string in, but the out put is tricky, we can return the last node that valid
# then, for serach, we can check if the last node is the last char, but it requrie the node carry extra val attribute
        