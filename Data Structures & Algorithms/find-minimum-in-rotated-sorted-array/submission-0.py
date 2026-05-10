class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if we want login, we need to reduce the search space more agreesively
        # then binary search on a rotatated array become the problem
        # if we calulate mid and check the condition, the left and right both can greater than the mid,
        # 1. so at least we want to make sure we dont miss hte minimum
        # 2. the search should be adaptable for unrotated array

        # I am not sure if I should start with an example simulation or high level approach
        # one example can be 
        # left mid right

        # if mid < left and right
        # then we only need to keep the range from left to mid

        # if left < mid < right
        # then the same

        # so one trick we can apply is:
        # we check the first and last element, to find if this is a rotated array, then we can early return or process for single case whch solve problem #2
        # I dont know if this is a proper strategy or hard coding

        # so for rotated array, seems like we always need to care about left region, 
        # if left > mid > right: then it might fail if right is not the minimum
        # if left < mid < right: same
        # so only safe choice is 
        # left > mid, right > mid, but left and right dont have to have certain relationship

        # for choice of bianary search, we can l < r - 1 + post process feels safe but I want to try with l < r. since it will converage to a single result
        # then we need a inbalanced rule since l < r is driving by one side agressive approach
        # we dont have a target, so we probably need to compare with l and r
        # if mid < l -> minmum in range (l,mid)
        # mid > l, then l has to be the mimimun
        # if right < mid, then r has to be the minimun
        # if right > mid, then we can skip the area from mid to r
        # this feels strange
        # how about, check left and right for this mid
        # if mid - 1 > mid > mid + 1, so we are in the decresing trend, them, we more r to this mid
        # if revwese, then we move l
        # if mid -1 > mid and mid + 1 > mid. then the mid should be the mimimum
        # another thing is we have to make sure it has mid - 1 and mid + 1
        # so we can futher simpify it as only conpare with the prev, 
        # if prev < mid, so the mid is in the incrasing trend, then we move right to mid since mid is not the minimum, we can do agressive on this
        # if prev > mid, so we move left to the mid, but here mid can be the minimum
        # since mid = (l+r)//2 is left-baised, we probably need to shift it to right-baised, then use r = mid -1
        # in this case, we no longer need to handle ;if mid -1 > mid and mid + 1 > mid. then the mid should be the mimimum'
        # because if prev > mid, we would make l = mid, then next term, mid is on the right, so it mid will coverage to the minimum as I guess
        # if prev > mid > next, it's not safe to move l to mid + 1 since mid still can be minimum
        # if prev < mid < next it's safe to move l to mid - 1 since we know mid is impossible to be minimum
        # but what if prev == mid, this is impossible before prev is not l, it is mid - 1
        # what if mid reach out 0 or len(nums) - 1, I think it will automatically means the mid is the minimun if we shrinking the space properly?
        # okay, this is wrong since I mis-imagine the array, both part of this should be ascending
        # so prev mid nxt wont work because it can happen in the first part or second
        # then for a rotate array, the thing we need to pay attention just like the early exit logic which is 
        # in the fist part, all nums should greater than nums[0], in the second part, all nums should less than nums[0]
        # in this case, if mid > l, it is in the first part, we should move l to mid, in this case, we can move it to mid +1 since the anwser is in the second part
        # if mid < l, its in the second part, we can move r to mid, here mid - 1 is not safe
        # I dont know mid == l, it might happen when we use left-bias mid
        # so it can be  prev, minmum... in this case, l land in prev, we need to move l to minimum as mid + 1
        # also can be ...minimum, next... in this case, we need to move r to minimum, 
        # so its a tricky problem probably something wrong here, one way might be we use l + 1 < r
        # then we post process the l and r, return min of them, but feel like we didnt solve the problem by avoiding it

        

        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l + 1 < r:
            
            mid = (l+r)//2
            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] >= nums[l]:
                l  = mid
        
        return min(nums[l],nums[r])

 

                 
            


