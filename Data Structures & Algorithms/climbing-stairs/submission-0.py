class Solution:
    def climbStairs(self, n: int) -> int:
        # in each step, you can choose jump or not jump if prev step if not. 
        # but we dont count no jump, we only count jump 1 or 2
        # for any position i, the way to get i is from i - 1 or i - 2
        # so partition[i] = partition[i - 1] + partition[i-2] + 1
        # before the first step, we can have a 1 ahead, 

        curr = [1]*(n + 1)
        for i in range(2, n + 1):
            curr[i] = curr[i-1] + curr[i-2]
        print(curr)
        return curr[-1]



