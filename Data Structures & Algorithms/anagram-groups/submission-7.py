class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def count(word):
            char_count = [0]*26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            return tuple(char_count)
        
        anagram_groups = defaultdict()

        for word in strs:
            char_count = count(word)
            if char_count in anagram_groups:
                anagram_groups[char_count].append(word)
            else:
                anagram_groups[char_count] = [word]
        
        return list(anagram_groups.values())

    


        