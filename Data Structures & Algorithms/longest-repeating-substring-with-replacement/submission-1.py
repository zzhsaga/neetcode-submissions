class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # in one substring, we sperate it into two part, major char and minor chars, 
        # we can think of a non-dup substring with k tolerance
        # so we need a counter-ish ds to track current minor chars
        # BF: for each l, we can get the longest substring until expanding r make it invalid, 
        #     then move to the next l and make this substring 
        # so this problem similar as the last one for BF as 
        # expanding r, until invalid, move l, make valid, keep exploring
        # the only thing is the last question, we can easily to use hashmap to move l to current dup
        # here we can use the same logic which we track the first minor char, but its tricky since we dont know if this move change which major and whats minor or not
        # another unique logic here is we have to track the major char, for simplicity, we can use use sum - max on the values, but it might not be optimal,
        # sum we can replace to window length such as r - l + 1, 
        # for max, we can use one varable to track, but its trickier, since when we move l, it will potaintially change what the max is 
        # for example, if 'A' is the major char, when we move l, it become minor, the current window can be valid...or not possible?
        # the delay update might work but I cant think through it entirely

        l = 0
        counter = Counter()
        longest_len = 0

        for r in range(len(s)):
            counter[s[r]] += 1

            while r - l + 1 - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            longest_len = max(longest_len, r - l + 1)
        
        return longest_len

        