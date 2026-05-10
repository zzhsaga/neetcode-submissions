class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # it's similar as the permutation, but with dynamic window, 
        # one intuition might be use r to extend the window until it become valid
        # then move l to shrink the window and keep it valid

        # this way we can get one valid substring, but how to get the mimum one,
        # one thought is current l in the position that move left one position would casue invalid, so we need to find the element on the right side of r, so it will be replaced

        # one thing i am not sure, when we move l if we make everything clean, basically means if l move, can we make sure all the position before l no longer be consider anymore.
        if len(t) > len(s):
            return ""
        counter = Counter(t)
        needed = len(counter)
        mini_substring = ""
        # print(counter)
        l = 0
        # for each r extendion, we check if current r in counter, and if check can pass, we try to move l
        # inside the loop, we update the mini_substring by current pointers
        # one thing is I wasnt include l = r so that was missing cases, but I dont know this at the first place
        # just intuitionaly to choose l < r, might be some over simplified or pattern memorization problem here
        # then we prepare to pop this l by updating the counter then move l to l + 1
        # i think the order doesnt matter inside the while loop but it feels more clean by following update -> revmove from counter -> move pointer
        # next step is the check function, right now is O(k) k == unique letters in the t
        # the problem is we dont have a straightforward way to track if any count greater than 0, so we need a data structure for quick loopup this
        # we can use another counter named needed, but I feel for minimulist and simplication, we can use a set, if any + or - make counter greater or less than 0, we should add/remove it in the needed
        # in details, we need to double the access freq to counter at least but for checking, we only need O(1) to add/remove/lookup set so we can get rid of the checking function
        # the whole iteration time, counter was changed at most 2len(s) times, so this should be a valid optimization and good scalarbility
        # futher optimization might be, is the set nessasary to be a set, since we only need to know if current window is valid or not, instead of which exactly char make it valid or not, we can simplifed it to a int
        # consider if any negetive happen here for needed... since we only -- needed when requrement is just get satisfied, so counter go to negative wont trigger needed change in theory
        for r in range(len(s)):
            # print(r,s[r],needed,counter)
            curr = s[r]
            if curr in counter:
                counter[curr] -= 1
                if counter[curr] == 0:
                    needed-=1
            while l <= r and needed == 0:
                # print(s[l:r+1],needed)
                
                # why the order was wrong?
                if not mini_substring or r - l + 1 < len(mini_substring):
                    mini_substring = s[l:r+1]
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] > 0:
                        needed += 1
                l += 1
            # print(l,r)
        return mini_substring
        


                    




