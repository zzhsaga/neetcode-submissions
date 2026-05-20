class Node:
    def __init__(self,is_end = False):
        self.children = {}
        self.is_end = is_end

class WordDictionary:
    # compare with defualt dict, we have to handle wild card charactor '.'
    # a brute force way might be for each adding word, we add all possible wild card anwsers
    # or we can use Trie, but we need to customize the search function
    # we can use BFS or DFS-ish search approach, for BFS, when we met a wild card, we insert all children in the deque
    # then we need a is_end attribute to mark if this is a end char
    # when checking one word, if we could go through all chars and the last char is end char, then we return true

    def __init__(self):
        self.trie = Node()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        # the logic is, we first have a deq, for each char, we check all the valid children and put them into deq for next char check
        # for each turn, we first check if word is running out and the curr is end, then if char in curr.children, if char is wild card, we add all children in deq
        # one concern is I feel the step didnt synced well since we used to check at the end,
        # one example, if word = 'a' and it is exist, in the first run, the i == len(word) - 1 but curr is not end because it is start node not the a node yet. so the trie logic we used to have is like start - a(we stop here), for n length node, we visited n + 1 nodes since start is always visited
        # so we need to move this terminate check at the end, but what if curr is not enough since deq might still contain multiple nodes, we prob need to check all of them
        deq = deque([self.trie])
        for i, char in enumerate(word):
            for _ in range(len(deq)):
                curr = deq.popleft()
                if char in curr.children:
                    deq.append(curr.children[char])
                if char == '.':
                    for child in curr.children:
                        deq.append(curr.children[child])
        for _ in range(len(deq)):
            curr = deq.popleft()
            if curr.is_end:
                return True
        return False
        
