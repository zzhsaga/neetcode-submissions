class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # the goal is checking if a substring of s2 contains all chars of s1
        # a counter-ish data structure might be useful since we can extract the char distribution of s1
        # the window size is fixed, so we dont need to worry about special moving logic
        # one straight forward approach is using s1 size window to scan on s2, check if any valid
        # optimization:
        # since we only have letters, we can use a list isntead of counter, then we can leverage with python = for list
        # but it might be O(26), do we have something can do O(1)?
        # back to counter solusion, counter/dict has a good feature that when one reach to 0, we can remove the key
        # so we only need to check if there is any key remaining which should be O(1)

        counter = Counter(s1)
        for i in range(0,len(s1) - 1):
            counter[s2[i]] -= 1
            if counter[s2[i]] == 0:
                del counter[s2[i]]
        # print(counter)
        for i in range(len(s1) - 1, len(s2)):
            # print(i)
            counter[s2[i]] -= 1
            if counter[s2[i]] == 0:
                del counter[s2[i]]
            if len(counter) == 0:
                return True
            prev = i - (len(s1) - 1)
            # print(i,prev,counter)
            counter[s2[prev]] += 1
            if counter[s2[prev]] == 0:
                del counter[s2[prev]]
            # print(i,prev,counter)
            
        return False


