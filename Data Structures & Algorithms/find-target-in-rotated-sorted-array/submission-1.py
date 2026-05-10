class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l = 0
        r = len(nums) - 1

        # binary serach design 
        # if unsorted, we can use l <= r
        # mid < target, l = mid + 1, else mid = r - 1(
        # or any l < r, make +1/-1 side not has equal is fine, then check if the final element is the target
        # if sorted
        # if target is in the same part of array, then the logic is the same, 
        # if target is in the another part of array, then target always greater or smaller than mid
        # let's see if there is condition can apply on both part
        # if target in 1st, and mid in second, mid < target r =  mid - 1
        # if target in 1st, and mid in first, if mid < target, l = mid + 1 as unsorted
        # if mid in 1st, and target in second, mid > target l =  mid + 1
        # if target in second, and mid in the scond, if mid > target, r = mid - 1
        # seems like the traditional way not work
        # one intuition might be, we seperate it to two step, first determine if it is a rotated array
        # if so, we find the minimum using binary serach
        # then we use another binary search on this unrotated sub array 
        if nums[0] > nums[-1]:
            while l < r:
                mid = (l + r)//2

                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1
            if target >= nums[0]:
                r = l - 1
                l = 0
            else:
                r = len(nums) - 1
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        
        return -1