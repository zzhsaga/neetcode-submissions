class Solution {
    public int longestConsecutive(int[] nums) {
        // sort(nums), 
        // count the longest consecutive seq
        // O(nlogn)

        // consecutive seq => the longest = nums.length
        // longest: minimum of nums: mini + nums.length = maxi
        // only need to check from mini of nums to mini + nums.length
        // O(n)
        // traversal the nums, build a lookup set
        // from the minimal, we check the longest consectutive seq
        if (nums.length <= 1 ){
            return nums.length;
        }
        int ans = 0;
 
        HashSet<Integer> lookup = new HashSet<>();
       
        for (int num:nums){
            lookup.add(num);
        }

        for (int key:lookup){
            System.out.println(key);
            int curr = key;
            if (lookup.contains(curr -1)){
                continue;
            }
            int count = 1;
            while (lookup.contains(curr + 1)){
                curr += 1;
                count += 1;
            }
            ans = Math.max(count,ans);
        }

        return ans;
    }
}
