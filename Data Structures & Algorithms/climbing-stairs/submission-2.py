class Solution:
    def climbStairs(self, n: int) -> int:
        # in each step, you can choose jump or not jump if prev step if not. 
        # but we dont count no jump, we only count jump 1 or 2
        # for any position i, the way to get i is from i - 1 or i - 2
        # so partition[i] = partition[i - 1] + partition[i-2] 
        # before the first step, we can have a 1 ahead, feel works, but i dont know why

        dp = [1]*3
        i = 0
        for i in range(2, n + 1):
            i = i%3
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        return dp[i%3]



