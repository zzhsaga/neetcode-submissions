class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length <= 1 ){
            return nums.length;
        }
        Arrays.sort(nums);
        
        int ans = 1;
        int curr = 1;
        for (int i = 1; i < nums.length; i++){
            // System.out.println(nums[i] + ","+ nums[i-1]);
            if (nums[i] - nums[i-1] == 1){
                curr += 1;
            }
            else if (nums[i] == nums[i-1]){
                continue;
            }
            else {
                curr = 1;
            }
            // System.out.println(curr);
            ans = Math.max(ans, curr); 
        }
        return ans;
    }
}
