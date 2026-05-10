class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // traverse the whole array -> hashmap, elemt <-> count 
        // top k in a array problem
        // 1. sort
        // ie. biggest count -> element
        // [(count, element),...] sort base on count -> pick top k
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num: nums) {
            countMap.put(num,countMap.getOrDefault(num,0)+1);
        }
        List<Map.Entry<Integer, Integer>> entryList = new ArrayList<>();
        
        for (Map.Entry<Integer, Integer> entry:countMap.entrySet()){
            entryList.add(entry);
        }

        entryList.sort((a,b) -> b.getValue() - a.getValue());

        int[] res = new int[k];
        for (int i = 0; i < k; i++){
            res[i] = entryList.get(i).getKey();
        }

        return res;


        
    }
}
