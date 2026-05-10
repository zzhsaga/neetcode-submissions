class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we need to use two pointers
        # l is the left boundary, r is the right boundary, we want to make sure the substring between them is valid
        # for helper data structure, we wnat something can record the freq of char in this substring
        # counter should be a good choice in this case
        # so the logic is, we have a major charactor that have highest freq, after the highest one, all the sum freq should small or equal to k
        # we can use sum(counter.values) - max(counter.values)
        # it might not be the best choice but we can start with it
        def check():
            value_list = counter.values()
            return sum(value_list) - max(value_list) <= k
        longest_substring = 0
        counter = Counter()
        l = r = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            while not check():
                counter[s[l]] -= 1
                l += 1
            longest_substring = max(longest_substring,r-l+1)

        return longest_substring