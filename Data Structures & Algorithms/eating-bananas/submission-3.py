import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_to_eat(speed):
            time = 0
            for p in piles:
                time += math.ceil(p / speed)
            return time

        l = 1
        r = max(piles)

        while l < r:
            speed = l + (r - l) // 2

            if time_to_eat(speed) <= h:
                r = speed
            else:
                l = speed + 1

        return l

        
        # question and concern:
        # i correct this several times to make it work
        # we starting with a speed area from 1 to max(piles)
        # then we calculate a current time cost and compare with h,
        # we want to make sure speed is minimun but make the time cost smaller than h
        # it's not straightforward how to move the pointer even though I can write the conditon as a template as alawys
        # ==, <, or >
        # but here, there is space to optimize even if == stands, so > should be agressively move but == or < should be maintain