class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1

        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
        
        for i in range(len(nums)):
            if zero_count > 1:
                nums[i] = 0
                continue
            
            if zero_count == 1:
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
                continue
            
            nums[i] = int(product/nums[i])
        
        return nums