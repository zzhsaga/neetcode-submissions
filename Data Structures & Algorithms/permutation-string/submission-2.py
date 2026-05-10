class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # feels like permutation is two string have exactly chars, probably same freq for each
        # so my intuition is fix a window length same as s1, scan s2 to see if any valid
        # the tricky part is checking, think if s1 is quite long and s2 is even longer, if we use counter which easy to collect freq, but hard to compare if two are the same
        # one way we can do is since they only contains letters, we can have two size 26 list to maintain since python has list equality

        s1_freq = [0]*26
        s2_freq = [0]*26

        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            s1_freq[ord(s1[i])-ord('a')]+=1
            s2_freq[ord(s2[i])-ord('a')]+=1
        
        if s1_freq == s2_freq:
            return True
        l = 0
        for r in range(len(s1),len(s2)):
            s2_freq[ord(s2[r])-ord('a')]+=1
            s2_freq[ord(s2[l])-ord('a')]-=1
            if s1_freq == s2_freq:
                return True
            l+=1
        return False