class Solution {
    public int[] productExceptSelf(int[] nums) {
        int nonZeroProduct = 1;
        boolean zeroExist = false;
        boolean allZero = false;
        for (int num:nums){
            if (num == 0){
                if (!zeroExist){
                    zeroExist = true;
                }
                else{
                    allZero = true;
                    break;
                }
            }
            else{
                nonZeroProduct = nonZeroProduct*num;
            }
        }
        int[] ans = new int[nums.length];
        if(allZero){
           return ans;
        }
        else{
            for (int i = 0; i < nums.length; i++){
                if (nums[i] == 0){
                    ans[i] = nonZeroProduct;
                }
                else if (zeroExist){
                    ans[i] = 0;
                }
                else {
                    ans[i] = nonZeroProduct/nums[i];
                }
            }
        }
        return ans;
        
    }
}  
