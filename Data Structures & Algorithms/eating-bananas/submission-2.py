import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_to_eat(speed):
            time = 0
            for p in piles:
                time += math.ceil(p/speed)
            return time
        
        if h < len(piles):
            return -1
        l = 1
        r = max(piles)

        #we want to find one that larger or equal to the condition, so we want the 
        #means we want the speed that t <= h

        while l < r:
            speed = (l+r)//2
            t = time_to_eat(speed)
            
            if t > h:
                l = speed + 1
            else:
                r = speed
            print(speed,t)
            print(l,r)
        
        return l

        
        # question and concern:
        # i correct this several times to make it work
        # we starting with a speed area from 1 to max(piles)
        # then we calculate a current time cost and compare with h,
        # we want to make sure speed is minimun but make the time cost smaller than h
        # it's not straightforward how to move the pointer even though I can write the conditon as a template as alawys
        # ==, <, or >