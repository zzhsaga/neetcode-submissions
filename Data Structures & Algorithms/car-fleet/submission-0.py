class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_to_s = {}

        for i, p in enumerate(position):
            p_to_s[p] = speed[i]

        position.sort()
        fleets = 0
        time = 0
        while position:
            curr = position.pop()
            curr_time = (target - curr)/p_to_s[curr]
            # print(time,curr_time)

            if not fleets or curr_time > time:
                fleets += 1
                time = curr_time
        
        return fleets
