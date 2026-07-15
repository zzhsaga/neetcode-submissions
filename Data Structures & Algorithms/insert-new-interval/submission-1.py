class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return
        ans = []
        added = False
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                ans.append(interval)
            elif interval[0] > newInterval[1]:
                if not added:
                    ans.append(newInterval)
                    added = True
                ans.append(interval)
            else:
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])
        if not added:
            ans.append(newInterval)
        return ans

    