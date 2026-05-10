class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # it's similar as the permutation, but with dynamic window, 
        # one intuition might be use r to extend the window until it become valid
        # then move l to shrink the window and keep it valid

        # this way we can get one valid substring, but how to get the mimum one,
        # one thought is current l in the position that move left one position would casue invalid, so we need to find the element on the right side of r, so it will be replaced

        # one thing i am not sure, when we move l if we make everything clean, basically means if l move, can we make sure all the position before l no longer be consider anymore.
        def check():
            for char in counter:
                if counter[char] > 0:
                    return False
            return True
        if len(t) > len(s):
            return ""
        counter = Counter(t)
        mini_substring = ""
        # print(counter)
        l = 0
        for r in range(len(s)):
            curr = s[r]
            if curr in counter:
                counter[curr] -= 1
            while l <= r and check():
                print(s[l:r+1])
                # why the order was wrong?
                if check():
                    if not mini_substring or r - l + 1 < len(mini_substring):
                        mini_substring = s[l:r+1]
                if s[l] in counter:
                    counter[s[l]] += 1
                l += 1
            # print(l,r)
        return mini_substring
        


                    




