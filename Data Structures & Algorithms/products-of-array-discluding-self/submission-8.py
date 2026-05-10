class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        product = 1
        for i in range(len(nums)):
            output[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= product
            product *= nums[i]

        # output = [0]*len(nums)
        # for i in range(len(nums)):
        #     output[i] = left_list[i]*right_list[i]
        
        return output