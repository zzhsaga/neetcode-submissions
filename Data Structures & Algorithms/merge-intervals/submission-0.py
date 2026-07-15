class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for interval in intervals:
            if not ans:
                ans.append(interval)
                continue
            last = ans[-1]
            #if overlap
            if last[0] <= interval[0] <= last[1]:
                last[0] = min(last[0], interval[0])
                last[1] = max(last[1], interval[1])
            else:
                ans.append(interval)
        
        return ans
# [[1,3],[1,5],[6,7]]

# [[1,3]]
# 1
# [1,5]
# 6
# [1,5],[6,7]