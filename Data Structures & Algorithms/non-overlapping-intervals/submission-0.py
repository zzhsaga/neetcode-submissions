class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        count = 0
        last = intervals[0][1]

        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0] < last:
                last = min(interval[1],last)
                count += 1
            else:
                last = interval[1]  

   
        
        return count
            
            