class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we can have a variable to track the longest substring so far, if current char can merge into this substring, we maintain it, if not we create a new one
        # the problem is, one dup show doenst mean the whole prev substring is invalid, we need to handle this more carefully
        # that was agressively to remove all prev substring, we should remove the char one by one from the beggning, so it is can get the maximum longest m valid substring
        # in case of doing this, we need to record the order as well, using two pointer might be a good way
        longest_len = 0
        curr_substring_set = set()
        l = r = 0

        for r, char in enumerate(s):
            while char in curr_substring_set:
                curr_substring_set.remove(s[l])
                l += 1
            curr_substring_set.add(char)
            longest_len = max(len(curr_substring_set),longest_len)
        
        return longest_len
