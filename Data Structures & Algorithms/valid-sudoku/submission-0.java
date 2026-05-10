class Solution {
    public boolean isValidSudoku(char[][] board) {
        // List<Integer> blockCheck = new ArrayList<>(); 
        List<Set<Integer>> rowCheck = new ArrayList<>(); 
        List<Set<Integer>> colCheck = new ArrayList<>(); 

        for (int i = 0; i < 9; i++){
            // blockCheck.add(new HashSet<>());
            rowCheck.add(new HashSet<Integer>());
            colCheck.add(new HashSet<Integer>());
        }
        for (int x = 0; x < 3; x++){
            for (int y = 0; y < 3; y++){
                Set<Integer> blockCheck = new HashSet<>();
                for (int m = 0; m < 3; m++){
                    for (int n = 0; n < 3; n++){
                        int currX = x*3 + m;
                        int currY = y*3 + n;
                        if (board[currX][currY] == '.'){
                            continue;
                        }
                        int curr = Character.getNumericValue(board[currX][currY]);
                        if (blockCheck.contains(curr)||rowCheck.get(currX).contains(curr)||colCheck.get(currY).contains(curr)){
                            return false;
                        }
                        else{
                            blockCheck.add(curr);
                            rowCheck.get(currX).add(curr);
                            colCheck.get(currY).add(curr);
                        }
                    }
                }
    
            }
        }
        return true;


    }
}
