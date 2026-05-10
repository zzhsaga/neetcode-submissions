class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> checkList = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++){
            if (checkList.contains(nums[i])){
                // System.out.println(nums[i]);
                return true;
            }
            else{
                checkList.add(nums[i]);
            }
        }
        return false;
    }
}
