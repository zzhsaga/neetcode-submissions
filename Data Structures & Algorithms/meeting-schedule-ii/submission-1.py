"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.start)
        count = 0

        schedule = []
        heapq.heapify(schedule)

        for interval in intervals:
            start = interval.start
            end = interval.end

            while schedule and schedule[0] <= start:
                heapq.heappop(schedule)
            
            heapq.heappush(schedule,end)

            count = max(count,len(schedule))
        
        return count
        