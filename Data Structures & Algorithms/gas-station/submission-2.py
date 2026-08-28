class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #  start with a subarrya that has largest summition
        diff = []

        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        if sum(diff) < 0:
            return -1
        
        diff = diff + diff
        # print(diff)

        start = 0
        curr_sum = 0
        max_start = 0
        max_sum = 0

        for i in range(len(diff)):
            curr_sum += diff[i]
            if curr_sum <= 0:
                start = i + 1
                curr_sum = 0
            elif curr_sum > max_sum:
                max_start = start
                max_sum = curr_sum

        return max_start