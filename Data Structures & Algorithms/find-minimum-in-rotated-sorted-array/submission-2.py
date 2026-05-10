class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] <= nums[-1]:
            return nums[0]
        # exclude the unrotated case

        l = 0
        r = len(nums) - 1

        # binary serach design 
        # l should be in the first part and r should be in the second,
        # then if l > mid, means mid is in the second part, we set l as mid + 1,it's not safe since the mimimum can between l and mid, so we should set r = mid to shrink the right region
        # if l <= mid, means mid is in the first part, which we should eliminate from the search space, so we set l as mid + 1
        # but the truth is in this setup, l can be in the second part, for example, 
        # in the first turn, mid is the maximum elment, then we move l to the minimum element, which in the second part
        # but the loop wont break yet since r can be the second element in the second part.
        # try to swithch to the r
        # if mid > r means mid is in the frist part, then we can move l = mid + 1
        # if mid <= r means mid is in the second part, then we can move r = mid
    
        while l < r:
            mid = (l + r)//2
            print(l,r,mid)
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]
 

                 
            


