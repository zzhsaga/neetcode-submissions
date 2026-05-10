class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # ## recap
        # goal: longest valid string
        # contraint: no dup chars
        # BF: for each i, try all substring that start from it until meet a dup, and maintain a maxi_len for updating the longest
        # why two pointers/sliding window?
        # for BF, for a new l, we scan all r that valid, but actually, if the prev_l is valid until prev_r, then l to prev_r is also valid, or all l between prev_l to prev_r is valid
        # so prev_l to prev_r is clean, our target shift to 'how to expand r' since right now moving r to futher right will make the substring invliad,
        # then we need to find a l that most left but can make r is able to expand
        # by repeating this, we can scan all the array
        # 1. fix l, move r until invalid
        # 2. fix r, move l until valid
        # back to 1
        # for tracking duplication, we need a data structure that easy to insert and delete, also support quick lookip
        # we should notice that the order acutally doesnt matter here because two pointers help us to tracking the position
        # but if we use hashset, we need to remove item one by one for l, we can futher accelarate by using hashmap which cache all the loccation of visited items
        # one tricky stuff here is if we move l to the new_pos, all the position between l and new_pos should be stale
        # one way to handle this is double check if s[r] in map also map[s[r]] >= l
        # so even though from the l, scan the right is a natrual approach I think that's how people get to learn for loop on array
        # but this question is acutally be framed as, for a r, what's the leftmost l to make it valid. 
        # I spend sometime to think how to turn BF into this because first time I learn this problem was using sliding window, bur I am not sure think through this make anything benefit
        
        substring_len = 0
        position_map = {}

        l = r = 0

        for r in range(len(s)):
            while s[r] in position_map and position_map[s[r]] >= l:
                l = position_map[s[r]] + 1
            position_map[s[r]] = r
            substring_len = max(substring_len, r - l + 1)
        
        return substring_len




