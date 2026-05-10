class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> checkMap = new HashMap<>();
        for (int i  = 0; i < nums.length; i++){
            if (checkMap.containsKey(nums[i])){
                return new int[]{checkMap.get(nums[i]),i};
            }
            else {
                checkMap.put(target - nums[i],i);
            }
        }
        return new int[]{}; // in case no solution is found
    }
}
