class Solution {

    public String encode(List<String> strs) {
        String encodedStr = "";
        for (String str:strs){
            for (int i = 0; i < str.length(); i++){
                char curr = str.charAt(i);
                encodedStr += curr;
                encodedStr += curr;
            }
            encodedStr += "01";
        }
        return encodedStr;
    }

    public List<String> decode(String str) {
        System.out.println(str);
        List<String> decodedStr = new ArrayList<>();
        String tmp = "";
        for (int i = 0; i < str.length(); i = i + 2 ){
            char curr = str.charAt(i); 
            char curr2 = str.charAt(i+1);
            if (curr != curr2){
                decodedStr.add(tmp);
                tmp = "";
            }
            else{
                tmp += curr;
                System.out.println(tmp);

            }
        }
        return decodedStr;
    }
}
