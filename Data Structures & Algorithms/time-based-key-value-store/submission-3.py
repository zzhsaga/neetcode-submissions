class TimeMap:
    # a data structure
    # 1. can store key and one pair of values 
    # 2. that can quickly look up with a parametor time, 
    # then we can consider to indexing the time stamp as second level key
    # when user look up the first level, it go into all the value under this key, then we should be able to support a good search algo to find the most recent value
    # for specifically we can reframe this search into a 
    # search the first element <= target, so it will be a typical () binary search
    # mid < target: keep
    # mid == target : keep or return
    # mid > target: aggresively move such as r = mid - 1
    # so the expected TC will be O(1) for inserting, O(logl) for look up, l stands for the length of specific list under one key 

    def __init__(self):
        self.nameMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.nameMap:
            self.nameMap[key] = [(timestamp,value)]
        else:
            self.nameMap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.nameMap or timestamp < self.nameMap[key][0][0]:
            return ""
        timeList = self.nameMap[key]
        if timestamp >= timeList[-1][0]:
            return timeList[-1][1]
        l = 0
        r = len(timeList) - 1
        while l < r:
            
            mid = (l+r+1)//2
            prev_timestamp, value = timeList[mid] 
            if prev_timestamp == timestamp:
                return value
            elif prev_timestamp < timestamp:
                l = mid 
            else:
                r = mid - 1
        
        return timeList[l][1]
        
