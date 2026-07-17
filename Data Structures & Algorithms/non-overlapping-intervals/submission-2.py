class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def return_end(interval):
            if not interval or not interval[1]:
                return 0
            return interval[1]
        if not intervals or len(intervals) < 2:
            return 0
        intervals.sort(key=lambda x: return_end(x))
        count = 0

        last_end = intervals[0][1]

        for i in range(1,len(intervals)):
            if intervals[i][0] < last_end:
                count += 1
            else:
                last_end = intervals[i][1]
        
        return count

        


            
            