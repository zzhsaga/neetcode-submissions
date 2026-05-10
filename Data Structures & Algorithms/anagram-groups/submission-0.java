class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> dict = new HashMap<>();
        for (String curr : strs){
            char[] currChars = curr.toCharArray();
            Arrays.sort(currChars);
            String sortedChars = new String(currChars);
            if (!dict.containsKey(sortedChars)){
                dict.put(sortedChars,new ArrayList<>()); 
            }
            dict.get(sortedChars).add(curr);
        }
        return new ArrayList<>(dict.values());
    }
}
