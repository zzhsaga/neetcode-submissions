class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return intervals
        ans = []
        i = 0
        n = len(intervals)
        added = False
        
        while i < n:
            if not added and intervals[i][1] >= newInterval[0]:
                if intervals[i][0] > newInterval[1]:
                    ans.append(newInterval)
                    added = True
                    continue
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
            else:
                ans.append(intervals[i])
            i+=1

        if not added:
            ans.append(newInterval)

        return ans
        
